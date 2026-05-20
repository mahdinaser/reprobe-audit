# MLE-bench

- arXiv: 2410.07095
- Repo: openai/mle-bench
- Source: ar5iv conversion **failed** — fell back to repository README
- Overall score: **0.30**

## Caveat
HTML conversion failure on `ar5iv.labs.arxiv.org/html/2410.07095`. Score is from the README only; the paper itself contains more methodological detail that we did not access through the automated pipeline.

## Identity (0.5)
- 75 Kaggle competitions; "Lite" variant with 22 competitions in the Low-complexity split.
- Grading: `mlebench grade` over a JSONL of `(competition_id, submission_path)`; "Any Medal (%)" metric.
- "Evaluation repeats with at least 3 seeds, reporting mean ± standard error of the mean."
- No structured benchmark version tag in README.

## Harness (0.5)
- Base Docker image: `mlebench-env` (built from `environment/Dockerfile`).
- Build command: `docker build --platform=linux/amd64 -t mlebench-env -f environment/Dockerfile .`
- README references three open-source agents but does not include their system prompts or tool inventories.
- No published image digest — locally-built `mlebench-env` will vary across builds.

## Inference (0.5)
- Leaderboard shows various LLMs (GPT-5, Gemini-3-Pro-Preview, Claude-Opus-4.6) but no specific configurations in the README.
- README does not pin temperature, sampling, or seed.

## Cost (0.0)
- No token or dollar cost figures in the README.

## Failure breakdown (0.0)
- No structured failure taxonomy in the README; per-competition success rates only.
