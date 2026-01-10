from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
from app.llm_router import generate_response

app = FastAPI()

@app.get("/")
def home():
    html = Path("app/templates/chat.html").read_text()
    return HTMLResponse(html)

@app.get("/chat")
def chat(q: str, session_id: str = "default"):
    return {"response": generate_response(q, session_id)}