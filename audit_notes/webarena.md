# WebArena

- arXiv: 2307.13854
- Repo: web-arena-x/webarena
- Source: ar5iv HTML
- Overall score: **0.50**

## Identity (0.5)
- 812 test examples (§3); evaluation methodology in §3.2.
- No explicit version tag or commit pinned to the headline numbers.
- No structured partial-credit policy.

## Harness (0.5)
- Agent variants named: "reasoning agent" vs "direct agent" (§4).
- System prompts in Appendix A.7 (verbatim).
- Max steps: 30 (A.5).
- No Docker image digest disclosed.

## Inference (1.0)
- "GPT-3.5-turbo-16k-0613, GPT-4-0613, and text-bison-001 with temperature of 1.0 and top-p of 0.9" (A.5).
- Pass count implicit (single pass per task).
- Missing: seed, evaluation date.

## Cost (0.0)
- No token counts, no dollar cost, no wall-clock.

## Failure breakdown (0.5)
- Qualitative error analysis in §5.2 and A.8 ("observation bias", "failures in observation interpretation").
- No structured per-task taxonomy with counts.
