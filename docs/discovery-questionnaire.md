# Discovery Questionnaire

Use this questionnaire with platform, application, network, storage, security and operations stakeholders. It is designed to surface migration blockers before a wave is scheduled.

## Business and ownership

- What business service does the workload support?
- Who is the application owner and technical owner?
- What is the criticality tier?
- What maintenance windows are permitted?
- What are the required RTO and RPO?
- Are there regulatory, data-location or contractual restrictions?

## VMware / compute

- Which vCenter, cluster and host group currently run the VM?
- Guest OS/version? Is it still vendor-supported?
- vCPU/RAM configured and observed peak/average utilization?
- CPU reservation/limit/affinity or latency-sensitive setting?
- NUMA, huge pages, PCI passthrough, GPU or special virtual hardware?
- VMware Tools dependence or guest customization assumptions?

## Storage

- Number, type and size of VMDKs?
- Actual used data versus provisioned capacity?
- Required IOPS/latency/throughput?
- Independent/shared disks or guest clustering?
- Snapshot/clone dependencies?
- Existing backup product and restore procedure?
- Data synchronization required during cutover?

## Network

- Port groups/VLANs and IP addressing?
- Can the IP change during migration?
- Default gateway and routing dependencies?
- Firewall rules and security zones?
- Load balancer/VIP/NAT dependencies?
- DNS records and TTL?
- External/partner allowlists tied to source IP?
- Required network throughput and latency?

## Application and data

- Application, middleware and database versions?
- Upstream/downstream dependencies?
- Hard-coded hostnames/IPs?
- Shared file systems or message queues?
- Authentication/AD/LDAP/PKI dependencies?
- Service startup/shutdown sequence?
- Application-level replication?

## Security

- Required segmentation/security groups?
- Endpoint/security agents and OS hardening requirements?
- Vulnerability/compliance controls?
- Encryption/key-management dependencies?
- Privileged-access process?

## Operations

- Monitoring platform and required agents?
- Central logging/SIEM integration?
- Backup and restore ownership?
- Patch/update mechanism?
- CMDB/asset-management integration?
- Incident/support escalation path?

## Acceptance and rollback

- What exact tests prove the service is healthy after migration?
- Who signs off the cutover?
- What condition triggers rollback?
- How long can rollback remain possible?
- How will data changed after cutover be handled if rollback is required?
