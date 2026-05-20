# MBPP

- arXiv: 2108.07732
- Source: ar5iv HTML
- Overall score: **0.88** (highest in the corpus)

## Identity (1.0)
- 974 short Python programs with test cases for semantic correctness.
- Curated subset of 426 hand-verified questions.
- Range: simple numeric operations to tasks requiring "nontrivial external knowledge."

## Harness (n/a)
- Non-agent evaluation.

## Inference (0.5)
- Models: 244M to 137B parameters.
- Temperature sampling with T=0.5 for synthesis; greedy decoding (T=0.0) for execution.
- 80 samples generated per problem for MBPP synthesis.
- Few-shot: 3 examples; fine-tuning on 374 problems for 100 steps.
- Not all seeds and hyperparameters disclosed beyond "seed 14 performs best".
- Learning rate specified only for 137B model: "3e-5".

## Cost (1.0)
- Energy and CO₂ for pre-training explicitly reported: "451 MWh and 26 tCO₂e".
- Fine-tuning costs noted as "comparably very small."

## Failure breakdown (1.0)
- Comprehensive error analysis: "Runtime errors are more common than syntax errors" for most model sizes.
- §4.10 identifies three failure categories: multi-constraint problems, more-common problem variants, and miscellaneous errors.
- "Linguistic off-by-one" errors documented where keyword overlap causes semantic drift.
- Categories named and grounded in specific problem types.
