#!/usr/bin/env python3
"""Aggregate REPROBE audit scores from a corpus CSV.

The CSV must have the columns:
    paper, arxiv_id, bic, hss, idp, crs, fmi, cprs, source

Field values are floats in {0.0, 0.5, 1.0} or the literal string "NA".

Prints:
    - per-paper score sheet (echoed back)
    - per-dimension mean, split by agent vs classical (HSS == NA)
    - overall CPRS mean

Usage:
    python score_corpus.py audit_results.csv
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from statistics import mean
from typing import Iterable


DIMENSIONS = ["bic", "hss", "idp", "crs", "fmi"]


def parse_value(raw: str):
    if raw.strip().upper() == "NA":
        return None
    try:
        return float(raw)
    except ValueError:
        return None


def load(path: Path) -> list[dict]:
    with path.open(newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        for d in DIMENSIONS + ["cprs"]:
            r[d] = parse_value(r.get(d, ""))
    return rows


def split(rows: Iterable[dict]) -> tuple[list[dict], list[dict]]:
    agent, classical = [], []
    for r in rows:
        if r["hss"] is None:
            classical.append(r)
        else:
            agent.append(r)
    return agent, classical


def col_mean(rows: list[dict], key: str) -> float | None:
    vals = [r[key] for r in rows if r[key] is not None]
    if not vals:
        return None
    return mean(vals)


def fmt(v: float | None) -> str:
    if v is None:
        return "  --"
    return f"{v:.2f}"


def print_sheet(rows: list[dict]) -> None:
    name_w = max(len(r["paper"]) for r in rows)
    header = ["paper".ljust(name_w)] + [d.upper() for d in DIMENSIONS] + ["CPRS"]
    print("  ".join(header))
    print("-" * (name_w + 8 * (len(DIMENSIONS) + 1)))
    for r in rows:
        cells = [r["paper"].ljust(name_w)]
        for d in DIMENSIONS:
            cells.append(fmt(r[d]).rjust(4))
        cells.append(fmt(r["cprs"]).rjust(4))
        print("  ".join(cells))


def print_aggregate(label: str, rows: list[dict]) -> None:
    print(f"\n{label} (n={len(rows)}):")
    for d in DIMENSIONS:
        v = col_mean(rows, d)
        print(f"  {d.upper()}: {fmt(v)}")
    print(f"  CPRS: {fmt(col_mean(rows, 'cprs'))}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", help="Path to audit_results.csv")
    args = parser.parse_args()

    path = Path(args.csv_path)
    if not path.exists():
        sys.stderr.write(f"Not found: {path}\n")
        return 2

    rows = load(path)
    if not rows:
        sys.stderr.write("Empty CSV.\n")
        return 2

    print("Per-paper sheet:\n")
    print_sheet(rows)

    agent, classical = split(rows)
    print_aggregate("Agent benchmarks", agent)
    if classical:
        print_aggregate("Classical (static) benchmarks", classical)
    print_aggregate("Overall", rows)

    return 0


if __name__ == "__main__":
    sys.exit(main())
