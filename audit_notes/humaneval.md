# HumanEval

- arXiv: 2107.03374 (the Codex paper)
- Source: ar5iv HTML
- Overall score: **0.75**

## Identity (1.0)
- 164 original programming problems with unit tests.
- Functional-correctness grading via unit-test execution.
- Released at `github.com/openai/human-eval`.

## Harness (n/a)
- Non-agent evaluation. HSS does not apply.

## Inference (0.5)
- Models: Codex variants (12M–12B), GPT-Neo, GPT-J, TabNine.
- Temperature: T=0.2 optimal for pass@1; T=0.8 for pass@100.
- pass@k metric, n=200 samples.
- No random seed.

## Cost (0.5)
- Training tokens: 100B.
- No inference dollar cost or wall-clock.

## Failure breakdown (1.0)
- Limitations section documents failures with long operation chains, variable-binding issues, and docstring comprehension problems.
- Synthetic task analysis provides categorized failures.
