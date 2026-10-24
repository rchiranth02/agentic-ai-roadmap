# phase-0-llm-hello

# Phase 0: LLM Hello + Order Extractor

- `hello.py`: first API call; prints reply, stop_reason, token counts
- `extract.py`: messy customer message -> validated JSON order, with one retry on bad output

Run: activate `.venv`, then `python extract.py`

Key lesson: the one real failure ("not an order") was an undefined business rule, not a model error.
