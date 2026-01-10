import json
import os
from collections import defaultdict

MEMORY_FILE = "memory_store.json"
MAX_HISTORY = 10 

_sessions = defaultdict(list)

if os.path.exists(MEMORY_FILE):
    try:
        with open(MEMORY_FILE, "r") as f:
            _sessions.update(json.load(f))
    except Exception:
        pass


def _persist():
    with open(MEMORY_FILE, "w") as f:
        json.dump(_sessions, f)


def add_message(session_id: str, role: str, content: str):
    _sessions[session_id].append({
        "role": role,
        "content": content
    })

    if len(_sessions[session_id]) > MAX_HISTORY:
        _sessions[session_id] = _sessions[session_id][-MAX_HISTORY:]

    _persist()


def get_history(session_id: str):
    return _sessions.get(session_id, [])