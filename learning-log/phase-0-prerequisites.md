Phase 0 — Prerequisites
Dates: 2026-10-21 → 2026-10-23 · Hours spent: ~ 2

Explain it like I'm new
An LLM (large language model) is a program that reads text and predicts what text should come next, one small piece at a time. You talk to it through an API: your code sends a request (which model, your message, some settings) and gets back a response (the model's reply plus info like how many tokens were used and why it stopped). The model has no memory between calls, so everything it needs to know must be in the request. You pay per token, both for what you send and what it writes back.

Key concepts
Token: the unit the model reads and writes. Roughly ¾ of an English word. Billing and limits are counted in tokens, not words.
Context window: the maximum number of tokens (input + output) the model can handle in one call. Send more and it fails or gets cut.
Input vs output tokens: input = everything I send (system prompt + messages). Output = everything the model writes, including hidden thinking.
System prompt: instructions that set the model's role and rules ("You are a pirate."). Sent with every call, so it costs tokens every time.
Temperature / sampling: the model picks the next token from a probability distribution, so the same prompt can give different answers. (My SDK version, anthropic 2.2.0, doesn't expose temperature, so I observed the default randomness instead.)
max_tokens: a hard cap on output length. The model doesn't plan around it; it just gets cut off.
stop_reason: why the model stopped. end_turn = finished naturally. max_tokens = cut off. Always check it before trusting output.
Content blocks: resp.content is a list of blocks, not one string. Blocks can be thinking, text, and later tool_use. Filter for text.
What I built
projects/phase-0-llm-hello/hello.py: loads my API key from .env, calls claude-haiku-5-5, prints the text reply, stop_reason, and input/output token counts. Each project has its own virtual environment (.venv) and requirements.txt.

Experiments
#	What I changed	What happened	Lesson
1	max_tokens=5	Reply cut to "A token is a small", stop_reason: max_tokens, 5 output tokens	max_tokens is a hard cut. Low limits will break structured output like JSON.
2	Same prompt ("one-line coffee shop tagline") run 3 times	3 different taglines, all variations of "Wake up, slow down, sip...". Output tokens 16 vs 18	Same input ≠ same output. One test run proves nothing; need multiple runs / an eval set (Phase 2).
3	Added system="You are a pirate."	"Arr, brew yer coffee strong, matey..." Input tokens 25 → 33	System prompt changes behavior a lot, and costs tokens on every call.
4	Same paragraph repeated 1×, 5×, 20× and summarized	Input: 102 → 430 → 1,660. Output: 62 → 65 → 142	Input cost scales with what I send. Output jumped at 20× because the model started thinking, and thinking tokens are billed as output.
What broke and which layer it was
See ../failure-log.md. Summary: all four bugs were Layer 4 (Harness): my code or setup didn't match the library or the response shape. None were the model being wrong.

Resources that actually helped
Anthropic docs (Messages API)
Reading the last line of a traceback first
Open questions
How does the model decide when to think? Can I control or turn it off?
How do I calculate the actual cost in $ from token counts?
-
