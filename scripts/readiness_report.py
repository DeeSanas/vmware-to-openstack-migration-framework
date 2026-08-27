#!/usr/bin/env python3
"""Generate a simple data-quality and migration-readiness summary from inventory CSV.

This intentionally performs transparent rules-based checks. It does not decide
whether a workload is technically safe to migrate.
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

REQUIRED_COLUMNS = {
    "vm_name",
    "application",
    "owner",
    "environment",
    "criticality",
    "guest_os",
    "vcpus",
    "ram_gb",
    "used_storage_gb",
    "disposition",
    "risk_flags",
}

REQUIRED_VALUES = (
    "vm_name",
    "application",
    "owner",
    "guest_os",
    "vcpus",
    "ram_gb",
    "used_storage_gb",
    "disposition",
)


def load_inventory(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        missing_columns = sorted(REQUIRED_COLUMNS - columns)
        if missing_columns:
            raise ValueError(
                "Missing required columns: " + ", ".join(missing_columns)
            )
        return [dict(row) for row in reader]


def report(rows: list[dict[str, str]]) -> int:
    dispositions = Counter()
    risks = Counter()
    incomplete: list[tuple[str, list[str]]] = []
    total_storage = 0.0

    for row in rows:
        vm_name = (row.get("vm_name") or "<unnamed>").strip()
        missing_values = [
            field for field in REQUIRED_VALUES if not (row.get(field) or "").strip()
        ]
        if missing_values:
            incomplete.append((vm_name, missing_values))

        disposition = (row.get("disposition") or "unclassified").strip().lower()
        dispositions[disposition] += 1

        for risk in (row.get("risk_flags") or "").split(";"):
            risk = risk.strip().lower()
            if risk:
                risks[risk] += 1

        try:
            total_storage += float((row.get("used_storage_gb") or "0").strip())
        except ValueError:
            risks["invalid-storage-value"] += 1

    print("VMware -> OpenStack Inventory Readiness Summary")
    print("=" * 48)
    print(f"Workloads: {len(rows)}")
    print(f"Used storage represented: {total_storage:,.1f} GB")

    print("\nDisposition summary:")
    for name, count in sorted(dispositions.items()):
        print(f"  - {name}: {count}")

    print("\nRisk flags:")
    if risks:
        for name, count in risks.most_common():
            print(f"  - {name}: {count}")
    else:
        print("  - none recorded")

    print("\nData-quality gaps:")
    if incomplete:
        for vm_name, fields in incomplete:
            print(f"  - {vm_name}: missing {', '.join(fields)}")
    else:
        print("  - required fields complete")

    # Nonzero means required inventory data is incomplete. Risk flags alone do
    # not fail because a risk is something to assess, not necessarily a blocker.
    return 2 if incomplete else 0


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} <workload-inventory.csv>")
        return 1

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"Inventory file not found: {path}")
        return 1

    try:
        rows = load_inventory(path)
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}")
        return 1

    return report(rows)


if __name__ == "__main__":
    raise SystemExit(main())
