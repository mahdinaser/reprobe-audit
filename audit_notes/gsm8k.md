# GSM8K

- arXiv: 2110.14168
- Source: ar5iv HTML
- Overall score: **0.50**

## Identity (1.0)
- "8.5K high quality linguistically diverse grade school math word problems."
- Split: 7.5K training, 1K test.
- Grading: "whether the final answer is correct."

## Harness (n/a)
- Non-agent evaluation.

## Inference (0.5)
- Models: GPT-3 6B and 175B.
- Temperatures: 0.0 for fine-tuning, 0.7 for verification.
- Sampling counts: 100 completions standard.
- Random seeds not specified beyond noting "seed 14 performs best" — not a structured per-experiment field.

## Cost (0.5)
- Token-level training info appears implicitly through batch sizes ("3.2 × 10⁴ tokens").
- Acknowledges OpenAI Supercomputing team usage; no explicit dollar cost or wall-clock breakdown.

## Failure breakdown (0.0)
- "Catastrophic mistakes" mentioned; "models frequently fail to accurately perform calculations."
- No systematic categorization with counts.
