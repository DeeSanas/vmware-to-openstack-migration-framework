# Migration Decision Matrix

The matrix below is a discussion tool, not an automated final decision engine.

| Condition | Rehost | Replatform | Refactor | Retain/Replace |
|---|---:|---:|---:|---:|
| Supported guest OS on KVM | Strong fit | Possible | Possible | If other blockers exist |
| Simple VM, few dependencies | Strong fit | Possible | Usually unnecessary | Rare |
| Unsupported/legacy OS | Risk | Possible if upgraded | Possible | Often consider retain/replace |
| Special VMware-only integration | Weak fit | Stronger candidate | Possible | Consider retain |
| Application modernization planned | Temporary option | Strong fit | Strong fit | Depends on roadmap |
| Very large data with tiny window | Possible with engineered sync | Possible | Possible | Timing may drive retain |
| Licensing/support tied to platform | Validate first | Validate | Validate | May drive retain/replace |
| Appliance/vendor VM with strict support | Only if vendor supports | Usually limited | Usually not applicable | Often retain/replace |

## Risk flags

Treat the following as reasons for deeper assessment:

- unsupported guest OS;
- physical/RDM/shared-disk dependencies;
- GPU/PCI passthrough;
- strict latency requirements;
- large data set with short outage window;
- unknown application owner;
- incomplete dependency information;
- hard-coded network identity;
- missing rollback procedure;
- application support contract restricted to VMware;
- source environment uses features with no direct target equivalent.

## Suggested wave classification

### Wave 0 — technical proof

Disposable/non-production test systems used to prove conversion, network, image, storage, monitoring and backup processes.

### Wave 1 — low-risk pilot

Supported systems with clear ownership, limited dependencies and straightforward rollback.

### Wave 2 — standard workloads

Typical application servers with known dependencies and tested runbooks.

### Wave 3 — complex/critical workloads

High business impact, large databases, special performance requirements, clustered systems or integrations requiring coordinated change.

### Retained set

Workloads not justified or technically suitable for migration in the current program. Retention should still have a documented reason, owner and review date.
