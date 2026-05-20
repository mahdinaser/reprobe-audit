# OSWorld

- arXiv: 2404.07972
- Repo: xlang-ai/OSWorld
- Source: ar5iv conversion **failed** — fell back to arXiv abstract + GitHub README
- Overall score: **0.30**

## Caveat
The HTML conversion on `ar5iv.labs.arxiv.org/html/2404.07972`
returned the "Conversion to HTML had a Fatal error" page. The
score below is from the arXiv abstract and the repository
README only, not from the full paper. A re-audit against the
PDF would likely move 1–2 cells.

## Identity (0.5)
- 369 tasks (from abstract).
- Supports Ubuntu, Windows, macOS environments.
- No structured version tag or grader-version reference in the README.

## Harness (0.5)
- README documents Docker provider: `provider_name: docker`, `os_type: Ubuntu` or `Windows`.
- `--max_steps 15` in the example invocation.
- No image digest pinned (only a provider declaration, which uses mutable upstream tags).

## Inference (0.5)
- README example: `--model gpt-4o`.
- No temperature, top-p, seed, or evaluation date documented in the README.

## Cost (0.0)
- No cost or token information in the README.

## Failure breakdown (0.0)
- No structured failure taxonomy in the README; `show_result.py`
  prints per-domain success rates.
