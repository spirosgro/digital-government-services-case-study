from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    ".github/workflows/validate.yml",
    "README.md",
    "CITATION.cff",
    "LICENSE.md",
    "LICENSE-CODE",
    "SECURITY.md",
    "analysis/service-prioritization.csv",
    "analysis/service-prioritization.md",
    "architecture/target-architecture.md",
    "docs/methodology-and-limitations.md",
    "governance/operating-model.md",
    "risk/risk-register.csv",
    "risk/security-privacy-register.md",
    "roadmap/implementation-roadmap.md",
    "references/references.md",
    "report/digital-government-services-case-study.docx",
    "report/digital-government-services-case-study.pdf",
    "presentation/digital-government-services-case-study.pptx",
    "presentation/digital-government-services-case-study.pdf",
]


def main() -> int:
    errors = []
    for relative in REQUIRED:
        path = ROOT / relative
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"Missing or empty: {relative}")

    public_extensions = {".md", ".csv", ".yml", ".yaml", ".cff", ".py"}
    forbidden = [
        re.compile("321" + r"[/\\-]?" + "2022034", re.I),
        re.compile("icsd" + "22034", re.I),
    ]
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in public_extensions:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in forbidden:
            if pattern.search(text):
                errors.append(f"Possible student identifier in {path.relative_to(ROOT)}")

    score_path = ROOT / "analysis" / "service-prioritization.csv"
    if score_path.is_file():
        with score_path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        if len(rows) != 5:
            errors.append("Expected five prioritised services")
        if sorted(int(row["rank"]) for row in rows) != [1, 2, 3, 4, 5]:
            errors.append("Ranks must be unique integers from 1 to 5")

    if errors:
        print("Repository validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("Repository validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
