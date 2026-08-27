#!/usr/bin/env python3
import csv
import sys
from pathlib import Path

REQUIRED = [
    "database_name",
    "engine",
    "version",
    "size_gb",
    "criticality",
    "rto_minutes",
    "rpo_minutes",
    "max_downtime_minutes",
    "owner",
]


def as_bool(value: str) -> bool:
    return value.strip().lower() in {"true", "yes", "1"}


def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "templates/database-inventory.csv")
    with path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))

    if not rows:
        raise SystemExit("No database inventory rows found")

    failed = False
    print(f"Databases assessed: {len(rows)}")
    for row in rows:
        name = row.get("database_name", "unnamed")
        missing = [field for field in REQUIRED if not row.get(field, "").strip()]
        if missing:
            print(f"FAIL {name}: missing {', '.join(missing)}")
            failed = True
            continue

        risks = []
        size = float(row["size_gb"])
        downtime = float(row["max_downtime_minutes"])
        critical = row["criticality"].strip().lower() == "critical"

        if size >= 1000:
            risks.append("large-data-set")
        if downtime <= 30:
            risks.append("low-downtime")
        if as_bool(row.get("replication_required", "false")):
            risks.append("replication-required")
        if as_bool(row.get("licensing_review", "false")):
            risks.append("licensing-review")
        if critical and not as_bool(row.get("ha_enabled", "false")):
            risks.append("critical-without-ha")

        label = ",".join(risks) if risks else "baseline"
        print(f"PASS {name}: {label}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
