# Security and privacy register

The register treats security, privacy, accessibility, availability, and supplier dependency as
service risks. Owners should convert each control into testable evidence before go-live.

| ID | Risk | Likelihood | Impact | Priority control evidence |
|---|---|---|---|---|
| R1 | Identity fraud or account takeover | High | High | MFA for staff, protected recovery, authentication logs |
| R2 | Excessive collection or retention | Medium | High | Data inventory, retention schedule, deletion test |
| R3 | Legacy integration failure | High | High | Contract tests, reconciliation, staged cutover |
| R4 | Outage or destructive cyber incident | Medium | High | Restore test, incident exercise, supplier escalation |
| R5 | Inaccessible resident experience | Medium | High | Accessibility audit, user testing, assisted channel |
| R6 | Supplier lock-in | High | Medium | Open interfaces, export test, maintained exit plan |
| R7 | Payment mismatch or duplication | Medium | High | Idempotency, segregation of duties, reconciliation |
| R8 | Low adoption | Medium | Medium | User research, staff involvement, adoption dashboard |

## Control baseline

- Use least privilege, separate staff and resident access paths, and review privileged access.
- Encrypt traffic and sensitive stored data; manage keys separately from application data.
- Centralise security logs and protect their integrity and retention.
- Maintain tested backups, recovery objectives, and an incident response playbook.
- Apply privacy by design, data minimisation, purpose limitation, and documented retention.
- Conduct a DPIA where the processing is likely to result in high risk.
- Test public channels against applicable accessibility requirements and publish an accessibility statement.
- Confirm whether national NIS2 implementation brings the municipality or a supplier into scope.

This is a design aid, not legal advice. The responsible authority must confirm Greek legal and
regulatory requirements for each service and procurement.
