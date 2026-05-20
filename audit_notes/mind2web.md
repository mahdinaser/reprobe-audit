# Mind2Web

- arXiv: 2306.06070
- Source: ar5iv HTML
- Overall score: **0.40**

## Identity (0.5)
- 2,350 tasks across 137 websites and 31 domains.
- Metrics: step success rate, task success rate.
- No explicit version pinning for the benchmark release.

## Harness (0.5)
- MindAct uses a fine-tuned DeBERTa-base for filtering and Flan-T5 variants for action prediction.
- Learning rates and batch sizes given for training.
- Multi-round element grouping described, but stopping criteria are not precise ("repeats until a single element is selected").

## Inference (0.5)
- Temperature: 0 for GPT models with three demonstration examples.
- Top-p, seed values, pass/attempt counts: not disclosed.

## Cost (0.0)
- Hardware mentioned ("4× A100 80GB cards", "A6000 48GB cards").
- No token counts, no monetary costs, no wall-clock for inference.

## Failure breakdown (0.5)
- Identifies that "the model's propensity to select the None option" hurts GPT-3.5.
- No structured taxonomy with counts.
