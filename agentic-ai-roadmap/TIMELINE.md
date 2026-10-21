# Timeline Estimate (3–6 hours/day)

**Bottom line:** ~150–260 focused hours total → **about 5–7 weeks at 6 h/day, 9–14 weeks at 3 h/day** (6 days/week).
A realistic target for most people: **~2.5 months at ~4 h/day.**

The roadmap's own table (12–18 weeks) assumes a part-time fresher at ~8–10 h/week. You're putting in 2–4x that, and you already
have Python, APIs, Git, CLI and data modelling from data engineering, so Phase 0 and Phase 7 compress a lot.

## Per phase

| Phase | Focus | Hours | Days @ 3 h | Days @ 6 h | Why this range |
|---|---|---|---|---|---|
| 0 | Prerequisites | 4–10 | 2–3 | 1–2 | You know Python/Git/APIs. Only LLM basics (tokens, temperature) + API key setup are new. |
| 1 | Foundation Model | 10–18 | 4–6 | 2–3 | Mostly reading docs + one comparison script. |
| 2 | Prompt Engineering | 15–25 | 5–8 | 3–4 | Building a 10–20 item eval set takes longer than expected. |
| 3 | Context / RAG | 25–40 | 8–13 | 4–7 | Biggest new-tech phase: embeddings, vector DB, chunking. Your pipeline instincts help. |
| 4 | Harness / tools | 20–35 | 7–12 | 4–6 | Tool calling, schemas, logging. Debugging agents is slow at first. |
| 5 | Loop / feedback | 15–25 | 5–8 | 3–4 | Hand-built ReAct loop, stop conditions, escalation. |
| 6 | Graph / coordination | 15–25 | 5–8 | 3–4 | DAG thinking is familiar (Airflow-style); the new part is a framework like LangGraph. |
| 7 | Ontology | 6–12 | 2–4 | 1–2 | This is data modelling. Your strongest phase. |
| — | Capstone | 40–70 | 13–23 | 7–12 | Combines everything; scope creep is the main risk. |
| | **Total** | **150–260** | **~51–85 days** | **~28–44 days** | |

Hours include ~20% for writing learning-log notes.

## Caveats (read these)

1. **6 h/day is rarely 6 focused hours.** Expect ~65–75% to be real progress; the rest is setup, rabbit holes, re-reading. If you
   plan on 6 h/day, budget against the 4–5 h column.
2. **Speed is the wrong metric past a point.** The roadmap's real goal is failure diagnosis, which only comes from hitting and
   fixing bugs. Rushing mini-projects to "check them off" skips the part that matters.
3. **Phases 3 and the capstone are where estimates blow up.** If you're 50% over on Phase 3, re-scope the capstone, don't extend it.
4. **Burnout risk at 6 h/day for 6+ weeks alongside other commitments is real.** 4 h/day with one rest day usually finishes sooner
   than 6 h/day with a two-week crash in the middle.
5. **API costs.** Comparing models and running eval sets costs money. Typically a few to tens of USD total if you use small models
   for iteration; set a spending cap on your API account.

## Suggested checkpoints (at ~4 h/day)

| End of week | Should be done |
|---|---|
| 1 | Phases 0–1 |
| 2 | Phase 2 |
| 4 | Phase 3 (RAG) |
| 5–6 | Phases 4–5 |
| 7 | Phases 6–7 |
| 9–10 | Capstone + write-up |
