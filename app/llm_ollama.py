import httpx

MODEL_NAME = "phi3"

def generate_response(messages):
    prompt = "\n".join(
        f"{m['role']}: {m['content']}" for m in messages
    )

    r = httpx.post(
        "http://localhost:11434/api/generate",
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )

    r.raise_for_status()

    text = r.json()["response"]
    text = text.lstrip().removeprefix("assistant:").strip()

    return text