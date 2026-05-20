# REPROBE — A disclosure audit schema for LLM agent benchmark runs

REPROBE is a small schema and codebook for recording, per result,
**what an LLM agent benchmark evaluation actually did**: which
benchmark version, which scaffold, which inference settings, what
it cost, and how it failed. This repository contains the schema,
the scoring codebook, a validator, an aggregation utility, two
example harness-hook patches, the raw scoring sheet from a
12-paper pilot audit, and per-paper extracted evidence.

The accompanying paper is *"What Twelve LLM Agent Benchmark Papers
Disclose About Themselves: A Pilot Audit and an Open Scoring
Schema"* (IEEE Big Data 2026 submission).

The motivation was specific. Two reports — one in a paper, one in
a blog post — claimed different SWE-bench Verified numbers for
nominally the same model from the same provider. We could not
recover from the published artifacts which scaffold, subset, or
inference configuration each had used. REPROBE is what we wrote
down so we would not be in that position again.

---

## Repository layout

```
reprobe-audit/
├── reprobe.schema.json     # JSON Schema (draft 2020-12) for the manifest
├── CODEBOOK.md             # field-by-field scoring rules
├── validate.py             # manifest validator (uses jsonschema)
├── score_corpus.py         # aggregation utility for audit CSVs
├── audit_results.csv       # 12-paper pilot audit scores
├── audit_notes/            # per-paper extracted evidence
│   ├── swe-bench.md
│   ├── webarena.md
│   ├── osworld.md
│   ├── gaia.md
│   ├── agentbench.md
│   ├── visualwebarena.md
│   ├── mind2web.md
│   ├── mle-bench.md
│   ├── humaneval.md
│   ├── mmlu.md
│   ├── gsm8k.md
│   └── mbpp.md
├── examples/
│   ├── minimal_manifest.json   # smallest valid manifest
│   └── swe_bench_example.json  # filled-in example
├── harness_hooks/
│   ├── swe_agent.patch         # illustrative SWE-agent patch
│   └── browsergym.patch        # illustrative BrowserGym patch
└── manifests/                  # drop manifests here for validation
```

---

## Quick start

### 1. Validate a manifest

```bash
pip install jsonschema
python validate.py examples/swe_bench_example.json
```

You should see:

```
examples/swe_bench_example.json   OK

1/1 valid
```

Or validate a whole directory:

```bash
python validate.py manifests/
```

### 2. Re-aggregate the pilot audit

```bash
python score_corpus.py audit_results.csv
```

You should see per-paper scores, per-group means, and the overall
mean. The agent-benchmark mean is **0.38**, the classical-benchmark
mean is **0.66**, and the overall mean is **0.47**.

---

## The schema

The schema has five disclosure fields plus a single aggregate
score:

| Field | What it asks |
|---|---|
| **Benchmark identity** | Which benchmark, version, subset, grader? |
| **Harness specification** | Scaffold, tools, stopping rule, environment image |
| **Inference settings** | Provider, model alias, sampling, engine, seed, run date |
| **Cost reporting** | Tokens, dollars, wall-clock |
| **Failure breakdown** | Per-category failure counts with task attribution |

Each field scores `1.0` (disclosed), `0.5` (partial), `0.0`
(absent), or `n/a`. The aggregate is the unweighted mean over
applicable fields. Scoring rules and boundary cases live in
[`CODEBOOK.md`](CODEBOOK.md).

A score of `1.0` means **"disclosed enough for a competent reader
to attempt a faithful re-execution"** — not "the experiment was
correctly designed." Disclosure is a necessary but not sufficient
condition for trustworthiness.

---

## The 12-paper pilot audit

The audit covered eight agent benchmarks and four classical
static benchmarks. Each paper was scored from the canonical
paper (read via `ar5iv.labs.arxiv.org` where the HTML conversion
succeeded, or the abstract + GitHub README where it did not)
plus the official repository.

| Benchmark | Identity | Harness | Inference | Cost | Failures | **Score** |
|---|---|---|---|---|---|---|
| SWE-bench | 0.5 | 0.0 | 0.5 | 0.0 | 0.0 | **0.20** |
| WebArena | 0.5 | 0.5 | 1.0 | 0.0 | 0.5 | **0.50** |
| OSWorld* | 0.5 | 0.5 | 0.5 | 0.0 | 0.0 | **0.30** |
| GAIA | 0.5 | 0.5 | 0.0 | 0.0 | 0.0 | **0.20** |
| AgentBench | 1.0 | 0.5 | 1.0 | 0.0 | 1.0 | **0.70** |
| VisualWebArena | 0.5 | 0.5 | 0.5 | 0.0 | 0.5 | **0.40** |
| Mind2Web | 0.5 | 0.5 | 0.5 | 0.0 | 0.5 | **0.40** |
| MLE-bench* | 0.5 | 0.5 | 0.5 | 0.0 | 0.0 | **0.30** |
| HumanEval | 1.0 | — | 0.5 | 0.5 | 1.0 | **0.75** |
| MMLU | 1.0 | — | 0.5 | 0.0 | 0.5 | **0.50** |
| GSM8K | 1.0 | — | 0.5 | 0.5 | 0.0 | **0.50** |
| MBPP | 1.0 | — | 0.5 | 1.0 | 1.0 | **0.88** |
| **Agent mean** (n=8) | 0.56 | 0.44 | 0.56 | 0.00 | 0.31 | **0.38** |
| **Classical mean** (n=4) | 1.00 | — | 0.50 | 0.50 | 0.62 | **0.66** |
| **Overall** (n=12) | 0.71 | 0.44† | 0.54 | 0.17 | 0.42 | **0.47** |

\* HTML conversion failed; scored from arXiv abstract + GitHub README.
† Mean is over the n=8 agent benchmarks for which the harness field applies.

Per-paper evidence and reasoning are in [`audit_notes/`](audit_notes/).

---

## What the audit found

- **Cost reporting is universally absent for agent benchmarks.**
  Eight of eight agent-benchmark papers in the corpus score 0.0
  on cost. The only paper in the corpus to fully disclose cost
  is MBPP, which reports training energy and CO₂ as a matter of
  disclosure policy in its corner of the literature.
- **No agent benchmark fully discloses its harness.** Seven of
  eight are partial; zero use content-addressed container
  digests. Mutable repository tags are used in their place
  across the agent-benchmark corpus.
- **Identity disclosure is the strongest field but with a split.**
  All four classical benchmarks reach 1.0; all eight agent
  benchmarks sit at 0.5 because benchmark version and
  subset-selection policy are not stated as structured fields.
- **Failure breakdown is the most heterogeneous field.**
  AgentBench's Table 4 is the canonical example of a fully
  disclosed failure breakdown; most agent papers offer
  qualitative analysis without counts.

The audit did not find a paper that misrepresented its
disclosures. Across the twelve papers, every 0.0 corresponded
to an omission — a field the paper template did not call for —
rather than a misstatement. This shapes the remediation
strategy: better instrumentation of evaluation harnesses, so
that disclosures are emitted automatically, rather than
stricter peer review of what was never written down.

---

## Limitations of this release

This is a 12-paper pilot, scored by a single auditor in one
pass. The codebook documents the partial-versus-disclosed
boundary rules we used; a second auditor could legitimately
move two or three cells. The cases where we were closest to
the boundary are flagged in the per-paper notes (the
AgentBench inference call of 1.0 vs. 0.5, the SWE-bench
harness call of 0.0 vs. n/a, the AgentBench cost call of 0.0
vs. 0.5).

A multi-rater audit with formal inter-rater agreement
(Cohen's κ) on a stratified sample of n=50–100 agent papers is
the natural next step, and we encourage anyone interested to
re-run the protocol against their own corpus.

Two papers in the intended corpus (OSWorld, MLE-bench) had
HTML-conversion failures on `ar5iv.labs.arxiv.org`; we fell
back to the arXiv abstract page plus the GitHub repository.
One paper (AgentBoard) we dropped because we could not access
enough text to score it fairly. A vendor blog announcing
SWE-bench Verified returned HTTP 403 and is excluded.

---

## How to use this for your own audit

1. **Read** `CODEBOOK.md`.
2. **Pick a corpus.** A stratified sample of recent agent
   papers from NeurIPS, ICLR, ACL is a reasonable target.
3. **Score each paper** by filling in a markdown file like
   those in `audit_notes/`, with a one-sentence justification
   per field citing the section of the paper or path in the
   repository that supports the score.
4. **Append to** `audit_results.csv` or maintain your own copy.
5. **Run** `python score_corpus.py your_results.csv` to get
   the aggregate.
6. **Open a pull request** if you want to contribute to a
   community-scale audit; we are interested in seeing how the
   per-dimension means shift with N.

---

## Citation

If you use this schema or the audit results, please cite:

```bibtex
@inproceedings{reprobe2026,
  title={What Twelve LLM Agent Benchmark Papers Disclose About
         Themselves: A Pilot Audit and an Open Scoring Schema},
  author={Anonymous},
  booktitle={IEEE International Conference on Big Data},
  year={2026}
}
```

---

## License

MIT.
