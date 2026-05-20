# AgentBench

- arXiv: 2308.03688
- Repo: THUDM/AgentBench
- Source consulted: `https://ar5iv.labs.arxiv.org/html/2308.03688` + repository README
- Overall score: **0.70** (highest among the agent-benchmark papers in the corpus)

## Identity (1.0 — disclosed)

- "8 distinct environments" (Section 1).
- Per-environment task counts and metrics in Table 2 (#Dev, #Test, SR/F1/Reward/Game Progress/Step SR).
- Explicit weighting formula: "reciprocal average score of all tested LLMs in each task as a fixed weight."

## Harness (0.5 — partial)

Disclosed:
- Prompting style: "Thought" and "Action" in one turn.
- System prompts in Appendix B.3 and C.3.
- Stopping rule: "maximum interaction turns" of 8–35 by environment.

Absent:
- No container/digest pinning for the environments. The
  environment is described per-task, but the build artifact for
  each environment is not version-pinned to a content digest.

## Inference (1.0 — disclosed)

Disclosed:
- "temperature=0 (i.e., greedy decoding)" — sampling method explicit.
- Model identifiers in Table 1.
- Implicit single pass per task (no aggregation rule needed).

Absent:
- Seed.
- Inference engine for open-weights models.
- Evaluation date.

**Boundary note.** We scored 1.0 rather than 0.5 because the
codebook's threshold ("sampling method and pass count clearly
stated") is met. One of us argued for 0.5 because seed and
engine are missing; we settled on 1.0 because the explicit
naming of greedy with temperature=0 and the single-pass
convention is more than the codebook threshold strictly
requires. This is the cell most likely to move under a second
auditor.

## Cost (0.0 — absent)

The paper mentions "approximately 4k and 13k calls for
inference, approximately the identical amounts of calls for
inference as MMLU requires."

No token counts, no dollar cost, no per-task wall-clock.

**Boundary note.** We considered 0.5 because the call count is
at least a structured quantity; the codebook says cost reporting
requires token-level or dollar-level disclosure, so we held the
line at absent.

## Failure breakdown (1.0 — disclosed)

Section 2 categorizes "five typical types" of failures:
- Context Limit Exceeded
- Invalid Format
- Invalid Action
- Task Limit Exceeded
- Complete

Table 4 quantifies the distribution across all eight
environments. Categories named (✓), counts per category (✓),
attribution to tasks (✓ — per environment).

This is the paper we used to calibrate what "disclosed" looks
like on the failure-breakdown field.

## Aggregate

`(1.0 + 0.5 + 1.0 + 0.0 + 1.0) / 5 = 0.70`
