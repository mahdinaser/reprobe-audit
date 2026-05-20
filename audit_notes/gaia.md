# GAIA

- arXiv: 2311.12983
- Source: ar5iv HTML
- Overall score: **0.20**

## Identity (0.5)
- 466 questions total; 166 in the developer set, 300 without annotations (§3.1).
- Grading uses "quasi exact match" without detailed partial-credit specification.

## Harness (0.5)
- System prompt in Figure 2 specifies output format.
- AutoGPT version reference limited to a git hash.
- GPT-4 plugins manually selected rather than systematically documented.
- Stopping rules not explicitly defined.

## Inference (0.0)
- Paper states "run the model three times and report the average results" — pass count yes.
- Temperature, top-p, seeds: not disclosed.
- Inference engine: not disclosed.
- Whole-field falls to 0.0 because the codebook requires sampling method + pass count, and sampling method is missing.

## Cost (0.0)
- No tokens, no cost, no wall-clock.
- Only human annotation timing noted ("two hours of annotator time").

## Failure breakdown (0.0)
- No structured taxonomy. §4 shows capability gaps without categorized failure counts.
