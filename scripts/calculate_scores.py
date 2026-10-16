from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "analysis" / "service-prioritization.csv"
WEIGHTS = {
    "citizen_value": 0.30,
    "operational_benefit": 0.25,
    "feasibility": 0.20,
    "compliance_simplicity": 0.10,
    "delivery_simplicity": 0.15,
}


def calculate(row: dict[str, str]) -> float:
    return round(sum(float(row[field]) * weight for field, weight in WEIGHTS.items()), 2)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    with CSV_PATH.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    errors = []
    for row in rows:
        calculated = calculate(row)
        recorded = float(row["score"])
        if abs(calculated - recorded) > 0.01:
            errors.append(f"{row['service']}: recorded {recorded:.2f}, calculated {calculated:.2f}")

    ranking = sorted(rows, key=lambda row: calculate(row), reverse=True)
    for index, row in enumerate(ranking, start=1):
        print(f"{index}. {row['service']}: {calculate(row):.2f} ({row['wave']})")

    if errors:
        print("Score errors:")
        print("\n".join(errors))
        return 1
    if args.check:
        expected_ranks = [int(row["rank"]) for row in ranking]
        if expected_ranks != list(range(1, len(rows) + 1)):
            print(f"Recorded ranks do not match calculated order: {expected_ranks}")
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
