# WER Calculation (Part 4, Question 12 - Problem set 1)

Small project demonstrating two ways to compute Word Error Rate (WER) between a reference and hypothesis sentence.

Files
- `wer_DP.py` — simple dynamic programming implementation that tokenizes input strings, computes WER and reports substitutions, insertions, deletions, and total reference words.
- `wer_JIWER.py` — example using the `jiwer` library (via `process_words`) to compute an alignment and WER metrics.

Prerequisites
- Python 3.8+ (or any modern Python 3.x)
- Project dependencies are listed in `requirements.txt` (install with pip).

Make a virtual environment (optional but recommended) and then do ` pip install -r requirements.txt` to install dependencies.


Usage
- clone or zip this repository.
- Run the dynamic-programming implementation: python wer_DP.py
- Run the jiwer-based example (requires `jiwer` in `requirements.txt`): python wer_JIWER.py


Both scripts print a small example using the same reference and hypothesis sentences and show WER and the S/I/D counts.

Notes
- The example reference/hypothesis are embedded in the scripts; to evaluate your own text, edit the `REF`/`HYP` variables in `wer_DP.py` or the `ref`/`hyp` variables in `wer_JIWER.py`.

