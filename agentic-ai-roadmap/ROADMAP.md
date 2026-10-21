# AI Agent Engineering Roadmap

_A phase-by-phase learning path for freshers_

A practical path from “I can call an LLM API” to “I can build and debug
real AI agents.” This roadmap is built around a 7-layer mental model for
AI systems engineering. Each layer is something an agent needs in order
to act safely and usefully — what it knows, what it can access, how it
recovers, and when it must stop. You'll learn the layers roughly in
order, but the real skill you're building is diagnosis: knowing which
layer a failure actually lives in before you touch anything.

## Phase 0 — Prerequisites

You need these basics before “agents” will make sense.

| **Area**     | **What to know**                                               |
|--------------|----------------------------------------------------------------|
| Python       | Functions, classes, error handling, working with JSON          |
| APIs         | REST basics, authentication, rate limits, reading API docs     |
| Git/GitHub   | Clone, commit, branch, push — enough to version your projects  |
| LLM basics   | What tokens, context windows, temperature, and sampling are    |
| Command line | Comfortable running scripts, installing packages, reading logs |

**Checkpoint project:** Write a Python script that calls an LLM API,
sends a prompt, and parses a structured JSON response. No agent behavior
yet — just a clean, working request/response loop.

## Phase 1 — Foundation Model

*Layer 1 → Capability*

**What this layer is:** Choosing the right model for the task and
understanding it well enough to predict where it'll fail.

### Learn

- The difference between model families/tiers (fast-and-cheap vs.
  slow-and-capable, reasoning-focused vs. general purpose)

- Context window size, multimodal support, and cost/latency tradeoffs

- Common failure modes: hallucination, inconsistent formatting,
  refusals, context overflow

- Why “benchmark leaderboards” matter less than testing your own task

### Do

- Run the same task across two or three different models and compare
  accuracy, cost, and speed

- Read the model documentation for at least one major provider
  end-to-end

### Mini-project

A “model picker” script that runs a task against two models, logs the
output, cost, and latency for each, and reports which one actually got
it right.

## Phase 2 — Prompt Engineering

*Layer 2 → Instructions*

**What this layer is:** Turning a vague goal into instructions specific
enough that success can be evaluated.

### Learn

- Zero-shot vs. few-shot prompting

- System/role prompts and how they shape behavior

- Step-by-step (chain-of-thought) reasoning prompts

- Structured output: JSON schemas, XML tags, output constraints

- Positive and negative examples (showing what NOT to do)

### Do

- Take a vague instruction and rewrite it with explicit constraints and
  success criteria

- Build a small evaluation set (10–20 example inputs with expected
  outputs)

### Mini-project

A prompt test harness — a script that runs several prompt variants
against your eval set and scores each one, so you can compare
objectively instead of guessing.

## Phase 3 — Context Engineering

*Layer 3 → Information*

**What this layer is:** Making sure the model has the right evidence,
memory, and tool results at the moment it needs to decide something.

### Learn

- Context window management: what to include, what to drop, what to
  summarize

- Retrieval-Augmented Generation (RAG): embeddings, vector databases,
  chunking strategies

- Short-term memory (conversation history) vs. long-term memory
  (persistent facts)

- Relevance and freshness — stale or irrelevant context is often worse
  than no context

### Do

- Learn one embedding model and one vector database (a lightweight/local
  one is fine to start)

- Build a basic RAG pipeline: chunk a document → embed it → retrieve
  relevant chunks → feed to the model

### Mini-project

A Q&A tool over a small set of your own documents (notes, PDFs) using
RAG.

## Phase 4 — Harness Engineering

*Layer 4 → Runtime*

**What this layer is:** The environment around the model — tools,
permissions, execution boundaries, state, and logs.

### Learn

- Tool use / function calling

- Defining permissions and execution boundaries (what is this agent
  actually allowed to touch?)

- Sandboxing and safe execution environments

- State management across multiple steps

- Logging and observability — you must be able to see why the agent did
  something

### Do

- Learn function calling / tool use in an SDK of your choice

- Build a small tool registry: 2–3 simple tools (e.g., calculator, file
  read/write, a search stub) with clear input/output schemas

- Log every tool call and model decision, not just the final answer

### Mini-project

An agent that can call 2–3 tools to complete a task, with a full,
readable log of every decision and tool call it made.

## Phase 5 — Loop Engineering

*Layer 5 → Feedback*

**What this layer is:** How the agent acts, checks its own results,
retries, and knows when to stop or ask for help.

### Learn

- The act → observe → decide loop (commonly called the ReAct pattern)

- Self-checking / verification steps before accepting a result

- Retry logic and backoff

- Explicit stopping conditions: max steps, cost caps, success criteria

- Escalation paths — when the agent should hand off to a human instead
  of retrying forever

### Do

- Implement a basic act-observe-decide loop by hand, without a heavy
  framework, so you understand the mechanics

- Add hard stop conditions and a “give up and ask a human” branch

### Mini-project

Take your Phase 4 agent and add a retry/verification loop with a hard
step limit and a clear human-escalation message. This is the single most
common place agents silently turn into expensive, useless loops — build
the stop condition first, not last.

## Phase 6 — Graph Engineering

*Layer 6 → Coordination*

**What this layer is:** Connecting multiple steps or agents through
dependencies, branches, and handoffs.

### Learn

- Sequential vs. parallel execution

- Conditional branching logic

- Handoffs between specialized sub-agents or sub-tasks

- Graph-based orchestration concepts: nodes = steps, edges =
  dependencies

### Do

- Sketch a workflow diagram (on paper is fine) before writing code for
  any multi-step task

- Learn one orchestration framework conceptually, even a simple one

### Mini-project

A workflow with at least one parallel branch and one conditional branch
— for example, “research” and “draft” run in parallel, then “review”
waits for both to finish before proceeding.

## Phase 7 — Ontology Engineering

*Layer 7 → Shared Meaning*

**What this layer is:** Defining the entities, relationships, and
business rules the system relies on. This is the layer most freshers
skip — and the one where the most confusing bugs come from.

### Learn

- Entity and relationship modeling

- Writing business rules as explicit, testable definitions rather than
  assumptions

- Schema design: what fields does a “customer” or “order” have, and what
  states can it move through?

- Why an unclear definition (e.g., “what counts as approved?”) can look
  exactly like a model bug

### Do

- Pick a domain (even a toy one) and write plain-language definitions
  for every core entity and state transition — e.g., “an order is
  'completed' when X, Y, and Z are all true”

- Turn those definitions into a formal schema (JSON schema or database
  schema)

### Mini-project

Write a short “ontology doc” for your capstone project's domain before
writing any agent code for it.

## The Cross-Cutting Skill: Failure Diagnosis

Once you've built something in each layer, practice this explicitly —
it's the actual point of the roadmap:

> *Before changing the prompt or switching models, identify where the
> failure actually lives.*

Some patterns to recognize:

- An unclear business definition can look like a model error → check
  Ontology before you touch the prompt

- A tool timeout can look like a reasoning failure → check Harness/logs
  before you touch the model

- A missing stop condition can turn a useful retry into an expensive
  loop → check Loop before you blame anything else

**Practice exercise:** Every time something breaks in your projects,
write one sentence naming which of the 7 layers it actually belongs to
before you fix it. This habit is what separates people who can build
agents from people who can only prompt-tweak until something works by
accident.

## Suggested Timeline

| **Phase** | **Focus**            | **Rough pace (part-time learner)** |
|-----------|----------------------|------------------------------------|
| 0         | Prerequisites        | 1–2 weeks                          |
| 1–2       | Model + Prompting    | 1–2 weeks                          |
| 3         | Context / RAG        | 2 weeks                            |
| 4         | Harness / tools      | 2 weeks                            |
| 5         | Loop / feedback      | 1–2 weeks                          |
| 6         | Graph / coordination | 1–2 weeks                          |
| 7         | Ontology             | 1 week                             |
| —         | Capstone             | 2–3 weeks                          |

Adjust freely — the order matters more than the pace.

## Capstone Project

Combine all seven layers into one end-to-end agent, for example:

- A research assistant that retrieves and cites sources (Context), uses
  tools to search and summarize (Harness), checks its own citations
  before finishing (Loop), runs research and drafting in parallel then
  merges them (Graph), and enforces a clear definition of what counts as
  a “verified” source (Ontology).

Document, for your own portfolio, which layer you'd blame for each bug
you hit along the way — that write-up is often more valuable to show
employers than the code itself.
