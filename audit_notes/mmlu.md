# MMLU

- arXiv: 2009.03300
- Source: ar5iv HTML
- Overall score: **0.50**

## Identity (1.0)
- 15,908 questions in total; dev (5 per subject), validation (1,540), test (14,079).
- 57 tasks across STEM, humanities, social sciences, and more.
- Grading: classification accuracy across all examples and tasks via multiple-choice (A–D).

## Harness (n/a)
- Non-agent evaluation.

## Inference (0.5)
- Models: GPT-3 variants, UnifiedQA, RoBERTa, ALBERT, GPT-2.
- Up to 5 demonstration examples with answers (few-shot count given).
- Prompt template stated: "The following are multiple choice questions (with answers) about [subject]".
- Temperature, sampling, seed: not specified.

## Cost (0.0)
- No tokens, no cost, no wall-clock.

## Failure breakdown (0.5)
- Identified weakness: "calculation-heavy STEM subjects tend to have low accuracy."
- Examples like GPT-3 "knows about PEMDAS" but fails to apply it.
- Not structured as a formal taxonomy with counts.
