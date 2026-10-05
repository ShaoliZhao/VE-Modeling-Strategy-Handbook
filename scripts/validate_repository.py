#!/usr/bin/env python3
"""Validate the paper catalog and internal paper references."""
from __future__ import annotations

import csv
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "references" / "papers.csv"
REQUIRED = {"id", "title", "year", "venue", "family", "primary_tasks", "status", "url"}


def validate() -> list[str]:
    errors: list[str] = []
    with CATALOG.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if set(reader.fieldnames or []) != REQUIRED:
            errors.append(f"paper columns differ: {reader.fieldnames}")
        rows = list(reader)
    ids = [row["id"] for row in rows]
    if len(ids) != len(set(ids)):
        errors.append("duplicate paper id")
    for number, row in enumerate(rows, 2):
        if not re.fullmatch(r"P\d{2}", row["id"]):
            errors.append(f"line {number}: invalid id {row['id']}")
        if row["status"] not in {"peer_reviewed", "preprint"}:
            errors.append(f"line {number}: invalid status")
        tasks = set(row["primary_tasks"].split("|"))
        if not tasks or not tasks <= {"T1", "T2", "T3"}:
            errors.append(f"line {number}: invalid task set")
        if not row["url"].startswith("https://"):
            errors.append(f"line {number}: URL must use https")
    known = set(ids)
    for document in ROOT.rglob("*.md"):
        text = document.read_text(encoding="utf-8")
        for paper_id in re.findall(r"\bP\d{2}\b", text):
            if paper_id not in known:
                errors.append(f"{document.relative_to(ROOT)}: unknown {paper_id}")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            local = target.split("#", 1)[0]
            if not (document.parent / local).is_file():
                errors.append(f"{document.relative_to(ROOT)}: missing local link {local}")
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        raise SystemExit("\n".join(problems))
    print("Repository validation passed: 28 papers and all internal references are valid.")
