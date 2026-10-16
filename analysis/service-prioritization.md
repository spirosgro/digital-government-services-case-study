# Service prioritisation

The case study compares five candidate municipal services on a five-point scale. The weighted
score supports sequencing; it does not replace discovery, legal review, user research, or cost
estimation.

## Criteria and weights

| Criterion | Weight | Interpretation |
|---|---:|---|
| Citizen value | 30% | Expected reduction in effort, delay, or uncertainty for residents |
| Operational benefit | 25% | Expected reduction in repetitive work, errors, or queue pressure |
| Feasibility | 20% | Availability of mature technology and manageable dependencies |
| Compliance simplicity | 10% | Relative ease of meeting privacy, legal, and audit obligations |
| Delivery simplicity | 15% | Relative ease of integration, procurement, rollout, and support |

Higher scores are better. Delivery simplicity is deliberately framed so that a high score means
lower implementation effort.

## Result

| Rank | Service | Score | Recommended wave |
|---:|---|---:|---|
| 1 | Infrastructure issue reporting | 4.28 | Pilot |
| 2 | Facility booking and appointments | 4.10 | Pilot |
| 3 | Digital certificate issuance | 3.95 | Integrate |
| 4 | Municipal debt payments | 3.85 | Integrate |
| 5 | Digital participation platform | 3.35 | Expand |

The pilot wave starts with services that create visible citizen value while limiting dependencies
on identity, payment, and registry systems. Certificate issuance and payments follow after the
integration and control foundation has been tested. Participation remains valuable, but adoption
and governance determine more of its outcome than technical delivery.

## Reproduce the ranking

```bash
python scripts/calculate_scores.py
```

The input values are explicit in `service-prioritization.csv`. Reviewers can change the scores or
weights and rerun the calculation.
