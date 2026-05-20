# VisualWebArena

- arXiv: 2401.13649
- Source: ar5iv HTML
- Overall score: **0.40**

## Identity (0.5)
- "910 diverse, natural, and visually grounded tasks" across three environments.
- Evaluation metrics in §3.3 (execution-based rewards).
- No explicit benchmark version pinning.

## Harness (0.5)
- System prompt: Appendix D provides full prompting instructions.
- Tool/action space: Table 1 lists actions (click, type, scroll, ...).
- Stopping rule: agents issue "stop [answer]" upon task completion.
- No container image digest.

## Inference (0.5)
- Models named: GPT-4, GPT-3.5, Gemini-Pro, LLaMA-2-70B, etc.
- "temperature of 1.0 and top-p of 0.9" for GPT; "0.6 and top-p of 0.95" for others.
- Pass count: single run implied; no explicit aggregation rule.
- No seed; no evaluation date.

## Cost (0.0)
- No token counts, no dollar cost, no wall-clock.

## Failure breakdown (0.5)
- Qualitative failure modes in §6.3 / Appendix A.3.
- Categories: task undoing, spatial reasoning errors, giving up early, looping behaviors.
- No quantified counts per category.
