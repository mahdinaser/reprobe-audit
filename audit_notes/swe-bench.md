# SWE-bench

- arXiv: 2310.06770
- Repo: princeton-nlp/SWE-bench
- Source consulted: `https://ar5iv.labs.arxiv.org/html/2310.06770` + repository README
- Overall score: **0.20**

## Identity (0.5 — partial)

Disclosed:
- "2294 software engineering problems" (Abstract).
- Data available at `https://www.swebench.com`.
- Evaluation criterion: "If the patch applies successfully and
  all of these tests pass we consider the proposed solution to
  have successfully resolved the issue" (Section 2.2).

Absent:
- No explicit version tag or commit hash bound to the reported
  numbers.
- No structured grader-version reference.
- No partial-credit policy field; evaluation is binary, which
  satisfies the spirit but not the structured form.

## Harness (0.0 — absent)

The paper does not propose an agent scaffold; it evaluates LLMs
directly with a prompt template (Appendix D.3). There is:
- no tool inventory in the harness sense,
- no stopping rule beyond "generate a patch",
- no environment image identifier.

**Boundary note.** This sat on the boundary between "absent" and
"n/a". We chose absent because the paper does describe an
evaluation procedure for LLMs; a reasonable auditor could mark
n/a instead.

## Inference (0.5 — partial)

Disclosed:
- Sampling method: "we simply use greedy decoding for all
  models" (Appendix D.2).
- Passes per task: "only generate a single patch per instance"
  (Appendix D.2).
- Models named: ChatGPT-3.5, GPT-4, Claude 2, SWE-Llama
  (Section 4.3).

Absent:
- Temperature value (greedy implies 0 but is not stated as a
  numeric field).
- Top-p, top-k.
- Seed.
- Inference engine for SWE-Llama.
- Evaluation date.

## Cost (0.0 — absent)

Only training compute is reported: "20 hours on 4 NVIDIA A100s"
(Appendix B.1, for SWE-Llama).

No per-instance token counts, no dollar cost, no inference
wall-clock.

## Failure breakdown (0.0 — absent)

Section 5.1 and Appendix F contain qualitative case-study
analysis ("models tend to write primitive Python code",
"generate shorter, simpler edits"). No named categories with
counts attributed to tasks.

## Aggregate

`(0.5 + 0.0 + 0.5 + 0.0 + 0.0) / 5 = 0.20`
