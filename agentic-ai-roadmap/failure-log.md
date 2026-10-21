# Failure Log

The roadmap's core skill is diagnosis: name the layer *before* fixing.

| Date | Project | What broke | Layer (1-7) | Why I think so | Fix |
|---|---|---|---|---|---|
| YYYY-MM-DD | phase-4-tool-agent | Agent "reasoned wrong" | 4 Harness | Log shows tool timed out, model guessed | Added timeout + error message to tool result |

Layers: 1 Model · 2 Prompt · 3 Context · 4 Harness · 5 Loop · 6 Graph · 7 Ontology
