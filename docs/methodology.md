# Migration Methodology

## Phase 1 — Discovery

Build a defensible inventory before discussing migration dates.

### Collect

- vCenter/cluster/host context;
- VM name, owner, environment and business service;
- guest OS/version and support status;
- configured and observed CPU/RAM;
- disks, used capacity and performance profile;
- network adapters, port groups, IPs and security dependencies;
- application/database/middleware dependencies;
- backup, replication and DR controls;
- maintenance window, RTO and RPO;
- licensing and vendor-support constraints.

### Deliverables

- workload inventory;
- dependency map;
- data-quality gap list;
- initial risk register.

## Phase 2 — Assessment and disposition

Assign each workload a migration disposition: rehost, replatform, refactor, retain, retire or replace.

Score factors such as:

| Dimension | Example question |
|---|---|
| Compatibility | Can the guest OS/app be supported on KVM/OpenStack? |
| Criticality | What is the business impact of outage or performance regression? |
| Dependency | Does the service require tightly coupled systems that must move together? |
| Data | How much data must be transferred and synchronized? |
| Network | Can IPs change? Are firewall/LB integrations known? |
| Operations | Are monitoring, backup and support models ready on target? |
| Licensing | Does virtualization-platform change affect license/support terms? |

## Phase 3 — Target design

Prepare the OpenStack platform before migration execution.

Define:

- projects/domains/RBAC;
- flavors and specialized aggregates;
- availability zones;
- image standards;
- Neutron tenant/provider networks;
- DNS/IPAM integration;
- Cinder/storage classes and performance expectations;
- security groups and external firewalls;
- logging/monitoring;
- backup and recovery;
- quota/capacity reserve;
- operational runbooks.

## Phase 4 — Pilot

Select workloads that are representative enough to expose integration issues but not so critical that the pilot creates unacceptable business risk.

Pilot objectives:

1. prove migration tooling/process;
2. measure data-transfer duration;
3. validate network/security mappings;
4. confirm guest drivers and performance;
5. exercise monitoring/backup;
6. prove rollback;
7. collect actual effort for wave planning.

## Phase 5 — Migration waves

Group workloads by application dependency and business change window, not merely by VM count.

Each wave should have:

- final source inventory snapshot;
- target capacity reservation;
- cutover method;
- data sync/freeze plan;
- network/DNS/firewall changes;
- acceptance tests;
- rollback threshold;
- named technical/business owners;
- communications plan.

## Phase 6 — Validation

Validate infrastructure and application outcomes. Include performance comparison where the workload has meaningful latency/throughput requirements.

## Phase 7 — Optimize and hand over

After stabilization:

- right-size flavors;
- remove temporary migration access/rules;
- verify backup retention;
- update CMDB/documentation;
- transfer operational ownership;
- close source resources only after retention/rollback obligations are satisfied;
- record lessons learned for later waves.
