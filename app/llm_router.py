from app.llm_groq import generate_response as groq_generate
from app.llm_ollama import generate_response as ollama_generate
from app.memory import add_message, get_history
import hashlib
import json

CACHE = {}

def _cache_key(session_id: str, messages: list) -> str:
    payload = {
        "session": session_id,
        "messages": messages
    }
    raw = json.dumps(payload, sort_keys=True)
    return hashlib.sha256(raw.encode()).hexdigest()


def generate_response(q: str, session_id: str = "default") -> str:
    add_message(session_id, "user", q)
    messages = get_history(session_id)

    key = _cache_key(session_id, messages)

    if key in CACHE:
        reply = CACHE[key]
    else:
        try:
            reply = groq_generate(messages)
        except Exception:
            reply = ollama_generate(messages)

        CACHE[key] = reply

    add_message(session_id, "assistant", reply)
    return reply