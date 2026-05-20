# REPROBE Codebook

Field-by-field scoring rules. Each field scores `1.0` (disclosed),
`0.5` (partial), `0.0` (absent), or `n/a` (not applicable).

The codebook is intentionally short. The hard cases are listed
explicitly; everything else should fall out naturally.

---

## 1. Benchmark identity

### identity / version
- **Disclosed (1.0):** A specific release tag, commit hash, or
  semver string is given.
- **Partial (0.5):** The benchmark name is given but no version
  identifier is bound to the reported result.
- **Absent (0.0):** Neither version nor commit referenced.

> Example partial: "We evaluate on SWE-bench Verified" — name given,
> version not.

### identity / subset
- **Disclosed (1.0):** Either an explicit `"full"` declaration with
  the matching cardinality, OR a numeric cardinality with a named
  subset rule (`first-100`, `random_seed_42`, `stratified`).
- **Partial (0.5):** Prose-only references like "we evaluate on
  the test set" without a cardinality binding.
- **Absent (0.0):** No information about which task set was
  evaluated.

### identity / grader_version
- **Disclosed (1.0):** A commit hash for code-based graders, OR a
  hash/version of the LLM-judge prompt and the judge-model
  identifier.
- **Partial (0.5):** Grader is described in prose without
  versioning.
- **Absent (0.0):** No grader description.

---

## 2. Harness specification

`n/a` for evaluations that do not involve an agent scaffold
(classical static benchmarks). For agent benchmarks, all
sub-fields below must be at least partially disclosed for the
field to clear partial.

### harness / scaffold
- **Disclosed (1.0):** Name + version (release tag or commit).
- **Partial (0.5):** Name only, no version pinning.
- **Absent (0.0):** Not described.

### harness / system_prompt
- **Disclosed (1.0):** Verbatim system prompt, or its SHA-256
  hash with a release artifact that contains the prompt.
- **Partial (0.5):** A description of the prompt without verbatim
  text or a verifiable hash.
- **Absent (0.0):** No system prompt information.

### harness / container
- **Disclosed (1.0):** A content-addressed container digest
  (e.g., `sha256:...`). Reproducibility is preserved across
  re-runs.
- **Partial (0.5):** A mutable repository tag (e.g.,
  `xlang-ai/osworld-env:latest`). The tag can be re-pushed
  against a different content hash.
- **Absent (0.0):** No container or build artifact referenced.

> This is the field that drives the agent–classical disclosure
> gap. Across the 12-paper pilot audit, zero agent benchmarks
> used digests.

### harness / max_steps (stopping rule)
- **Disclosed (1.0):** Explicit numeric bound.
- **Partial (0.5):** Range only ("between 8 and 35 by
  environment").
- **Absent (0.0):** No stopping rule documented.

---

## 3. Inference settings

### inference / sampling
- **Disclosed (1.0):** Sampling method named AND per-task pass
  count given.
- **Partial (0.5):** Sampling method named but pass count
  missing, OR pass count given but sampling not.
- **Absent (0.0):** Neither.

> Boundary case worth flagging: "We use greedy decoding for all
> models" without a per-task pass count is **partial**, not
> disclosed. This is the boundary case we hit most often during
> pilot scoring.

### inference / engine
- **Disclosed (1.0):** For open-weights models, the inference
  engine and version (e.g., `vllm-0.5.0`). For closed-API
  models, the provider's model alias *with* a run date.
- **Partial (0.5):** Closed-API alias without run date, OR
  engine name without version.
- **Absent (0.0):** No engine or version.

### inference / seed
- **Disclosed (1.0):** Seed value given, OR explicit `null`
  declaration that the provider does not expose a seed.
- **Partial (0.5):** Implicit (greedy decoding implies
  deterministic, but a seed is still required for sampled
  decoding).
- **Absent (0.0):** No mention.

### inference / aggregation (if passes_per_task > 1)
- **Disclosed (1.0):** Rule explicitly stated (mean, majority,
  best-of-N, with verifier identified if applicable).
- **Partial (0.5):** Aggregation happens but the rule is
  ambiguous.
- **Absent (0.0):** Multiple passes performed without disclosing
  how they were combined.

---

## 4. Cost reporting

### cost / tokens
- **Disclosed (1.0):** Input + output token counts (aggregate or
  per-task) reported.
- **Partial (0.5):** One of input/output but not both, OR a
  structured proxy ("approximately 4k calls").
- **Absent (0.0):** No token-level disclosure.

### cost / dollars
- **Disclosed (1.0):** Dollar cost reported with a stated rate
  source (URL of the pricing page).
- **Partial (0.5):** Dollar cost without rate source, OR rate
  source without computed dollars.
- **Absent (0.0):** No dollar cost.

### Whole-field rule
- **Disclosed (1.0):** At least one of `tokens` or `dollars`
  reaches 1.0, AND wall-clock time is given.
- **Partial (0.5):** Any structured cost-related number is
  reported.
- **Absent (0.0):** No cost information.

> Boundary case: a paper that reports `"approximately 4k and 13k
> calls for inference"` is borderline. We treat call counts as
> partial only if they are quantified; pure prose ("inference is
> expensive") is absent.

---

## 5. Failure breakdown

### Whole-field rule
- **Disclosed (1.0):** All three of: (a) named categories,
  (b) integer counts per category, (c) attribution to tasks or
  subgroups (not just to the corpus as a whole).
- **Partial (0.5):** Qualitative analysis OR named categories
  without counts.
- **Absent (0.0):** No failure-mode discussion.

> The canonical "disclosed" example is AgentBench's Table 4,
> which categorizes failures into Context Limit Exceeded,
> Invalid Format, Invalid Action, Task Limit Exceeded, and
> Complete, with counts per environment.

---

## Aggregate score

The aggregate is the unweighted mean of the applicable fields:

```
score = sum(s_d for d in applicable_fields) / |applicable_fields|
```

`n/a` fields are removed from the denominator.

A score of `1.0` means "disclosed enough for a competent reader
to attempt a faithful re-execution," **not** "the experiment was
correctly designed." Disclosure is a necessary, not sufficient,
condition for trustworthiness.

---

## Recording your work

For each field, write a one-sentence justification with a
citation to the section/line of the paper or the path in the
repository that supports the score. Store as
`audit_notes/<benchmark>.md`. See `audit_notes/swe-bench.md`
and `audit_notes/agentbench.md` for worked examples.
