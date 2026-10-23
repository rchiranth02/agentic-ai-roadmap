import os
from dotenv import load_dotenv
import anthropic

load_dotenv()  # reads .env so the key is in os.environ
client = anthropic.Anthropic()  # picks up ANTHROPIC_API_KEY automatically

paragraph = (
    "A data pipeline moves data from source systems into a warehouse. "
    "It usually extracts records, cleans and transforms them, and loads them "
    "into tables that analysts query. Good pipelines are idempotent, monitored, "
    "and fail loudly when the input data looks wrong. "
)
repeat = 20   # try 1, then 5, then 20
text = paragraph * repeat

resp = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=200,
    messages=[{"role": "user", "content": f"Summarize this in one sentence:\n\n{text}"}],
)
for block in resp.content:
    if block.type == "text":
        print(block.text)
print("stop_reason:", resp.stop_reason)
print("tokens in/out:", resp.usage.input_tokens, resp.usage.output_tokens)
