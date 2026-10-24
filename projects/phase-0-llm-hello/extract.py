import json
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

SYSTEM = """You extract order details from customer messages.

Return ONLY a JSON object. No explanation, no markdown, no code fences.

Use exactly these keys:
- "customer_name": string
- "items": list of objects, each with "product" (string), "color" (string), "size" (string), "quantity" (integer)
- "city": string
- "deadline": string, as written by the customer (e.g. "Friday")

Rules:
- If a field is not mentioned in the message, use null. Never guess or invent a value.
- "quantity" must be a number, not a word (write 3, not "three").
- If the message is not a product order, return exactly: {"not_an_order": true}

Example output:
{"customer_name": "Asha Rao", "items": [{"product": "mug", "color": "white", "size": null, "quantity": 2}], "city": "Mumbai", "deadline": null}"""

def call_model(text):
    resp = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=500,
        system= SYSTEM,
        messages=[{"role": "user", "content": text}],
    )
    # 1. Don't trust a cut-off answer: half a JSON object is useless
    if resp.stop_reason == "max_tokens":
        raise RuntimeError("Response was cut off. Increase max_tokens.")

    # 2. Collect only the text blocks (skip thinking blocks), same idea as hello.py
    raw = ""
    for block in resp.content:
        if block.type == "text":
            raw += block.text
    return raw

REQUIRED_KEYS = ["customer_name", "items", "city", "deadline"]

def parse(raw):
    # 1. Strip ```json fences, in case the model ignores the "no fences" rule
    text = raw.strip()
    if text.startswith("```"):
        text = text.strip("`")
        if text.startswith("json"):
            text = text[4:]

    # 2. String -> Python dict. Raises json.JSONDecodeError if it's not valid JSON
    data = json.loads(text)
    if data.get("not_an_order"):
        return data

    # 3. Validate: like a schema check on incoming data in a pipeline
    for key in REQUIRED_KEYS:
        if key not in data:
            raise ValueError(f"Missing key: {key}")
    for item in data["items"]:
        if not isinstance(item.get("quantity"), int):
            raise ValueError(f"Quantity is not an integer: {item}")
        if not isinstance(data["items"], list) or not data["items"]:
            raise ValueError("items must be a non-empty list")

    return data

def extract_order(text, max_attempts=2):
    prompt = text
    for attempt in range(1, max_attempts + 1):
        raw = call_model(prompt)
        try:
            return parse(raw)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"  Attempt {attempt} failed: {e}")
            # Tell the model what went wrong and try again
            prompt = (f"{text}\n\nYour previous answer was invalid ({e}). "
                      f"Previous answer:\n{raw}\n\nReturn corrected JSON only.")
    raise RuntimeError(f"Failed after {max_attempts} attempts")


TEST_MESSAGES = [
    "Hi, I'm Priya Sharma, I'd like to order 3 blue t-shirts size M, ship to Pune by Friday please.",
    "rahul here. need two black hoodies L and one red cap. delivery to bangalore asap",
    "Can I get a dozen white socks? Name's Meera K. Thanks!",                       # no city, no size
    "Order for Arjun: 1 green jacket XL + 4 grey t-shirts S, Chennai, before Diwali",
    "hey what are your store timings?",                                              # not an order at all
]

for msg in TEST_MESSAGES:
    print("\nINPUT:", msg)
    try:
        print("OUTPUT:", extract_order(msg))
    except Exception as e:
        print("ERROR:", e)