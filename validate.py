#!/usr/bin/env python3
"""Validate REPROBE manifest files against the schema.

Usage:
    python validate.py <path>
        <path> may be a single JSON file or a directory.
        If a directory, every *.json under it is validated.

Exit code 0 if all files pass, 1 if any fail.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    sys.stderr.write(
        "jsonschema is required. Install with: pip install jsonschema\n"
    )
    sys.exit(2)


SCHEMA_PATH = Path(__file__).resolve().parent / "reprobe.schema.json"


def load_schema() -> dict:
    with SCHEMA_PATH.open() as f:
        return json.load(f)


def collect_manifests(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    if target.is_dir():
        return sorted(target.rglob("*.json"))
    sys.stderr.write(f"Not a file or directory: {target}\n")
    sys.exit(2)


def validate_one(manifest_path: Path, validator: "jsonschema.Draft202012Validator") -> tuple[bool, str]:
    try:
        with manifest_path.open() as f:
            doc = json.load(f)
    except json.JSONDecodeError as e:
        return False, f"JSON parse error: {e.msg} at line {e.lineno}"

    errors = sorted(validator.iter_errors(doc), key=lambda e: e.path)
    if not errors:
        return True, "OK"

    # Concise error report: first error only, with path.
    first = errors[0]
    path = ".".join(str(p) for p in first.absolute_path) or "<root>"
    return False, f"{path}: {first.message}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Manifest file or directory containing manifests")
    parser.add_argument(
        "--quiet", action="store_true", help="Only print failures and a final summary"
    )
    args = parser.parse_args()

    schema = load_schema()
    validator = jsonschema.Draft202012Validator(schema)

    target = Path(args.path)
    manifests = collect_manifests(target)

    if not manifests:
        print(f"No manifests found at {target}")
        return 0

    failed = 0
    width = max(len(str(m)) for m in manifests)
    for m in manifests:
        ok, msg = validate_one(m, validator)
        if not ok:
            failed += 1
            print(f"{str(m).ljust(width)}   FAIL: {msg}")
        elif not args.quiet:
            print(f"{str(m).ljust(width)}   OK")

    print(f"\n{len(manifests) - failed}/{len(manifests)} valid")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
