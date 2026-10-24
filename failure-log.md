# Failure Log

The roadmap's core skill is diagnosis: name the layer *before* fixing.

| Date | Project | What broke | Layer (1-7) | Why I think so | Fix |
|---|---|---|---|---|---|
| 2026-10-23 | phase-0-llm-hello | `pip install` put packages in global Python, conflicting with streamlit | 4 Harness | No `(.venv)` in prompt; venv never activated | Created + activated `.venv`, reinstalled, regenerated `requirements.txt` |
| 2026-10-23 | phase-0-llm-hello | `TypeError: unexpected keyword argument 'temperature'` | 4 Harness | Code written for an older SDK; anthropic 2.2.0 has no `temperature` param | Removed the param. Check `pip show anthropic` + docs for the installed version |
| 2026-10-23 | phase-0-llm-hello | `NotFoundError 404: model: You are a pirate` | 4 Harness | System prompt text passed as `model=` instead of `system=` | Added `system=` as its own argument. Read last line of traceback first |
| 2026-10-23 | phase-0-llm-hello | `AttributeError: 'ThinkingBlock' object has no attribute 'text'` on long input | 4 Harness | Model returned `[thinking, text]`; code assumed `content[0]` was text | Loop over `resp.content`, print only blocks where `type == "text"` |

Layers: 1 Model · 2 Prompt · 3 Context · 4 Harness · 5 Loop · 6 Graph · 7 Ontology
| 2026-10-24 | phase-0-llm-hello | "store timings?" crashed: `'NoneType' object is not iterable` | 7 Ontology (+4) | Model returned items: null; we never defined what "not an order" looks like, and validation assumed items is a list | Added rule `{"not_an_order": true}` to prompt + non-empty list check in parse() |