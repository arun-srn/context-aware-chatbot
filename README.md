# Context-Aware Chatbot with Memory and Fallback Models

## Project Overview

This project implements a context-aware conversational chatbot designed to handle multi-turn conversations reliably.

The system maintains short-term conversational memory, supports automatic fallback between language models, and uses in-memory caching to reduce latency and API usage. If the primary cloud-based model fails, the chatbot seamlessly switches to a locally hosted model without interrupting the user experience.

The objective of this project is to demonstrate practical system design, reliability, and engineering trade-offs in conversational AI — not to train or fine-tune language models.

---

## Key Features

### 1. Multi-Turn Conversation Memory
- Session-based chat history is maintained
- Previous user and assistant messages are included in future prompts
- Enables coherent follow-up questions and context-aware responses
- Memory is stored in-memory for simplicity and speed

### 2. Primary + Fallback Model Architecture
- Primary model: Groq-hosted LLM (cloud-based, low latency)
- Fallback model: Ollama (locally hosted)
- Automatic fallback occurs if the primary model:
  - Fails
  - Times out
  - Encounters API, quota, or network errors
- Ensures uninterrupted responses even when external services fail

### 3. Lightweight Context Retrieval
- Relevant past messages are retrieved from the session history
- Retrieved messages are appended directly to the prompt
- No embeddings or vector databases are used
- Prompt-based retrieval is sufficient for short conversational context

### 4. Response Caching
- Frequently repeated user queries are cached in memory
- Cached responses are returned instantly
- Reduces latency, API calls, and external model usage costs

### 5. Simple Web-Based Chat Interface
- Lightweight frontend using HTML, CSS, and JavaScript
- User messages are right-aligned
- Assistant messages are left-aligned
- Clean, chat-style UI similar to common messaging applications

---

## System Architecture (High Level)

User (Browser)  
→ FastAPI Backend  

    ├── Cache (instant return if hit)
    ├── Session Memory
    ├── Primary LLM (Groq)
    │       └── on failure → Fallback LLM (Ollama)

---

## Technologies Used

- Backend: FastAPI (Python)
- Frontend: HTML, CSS, JavaScript
- Primary LLM: Groq API
- Fallback LLM: Ollama (local inference)
- HTTP Client: httpx
- Environment Management: python-dotenv

---

## How the System Works

1. User sends a message through the browser interface
2. The backend receives the message along with a session identifier
3. Conversation history for that session is retrieved
4. Cache is checked for an existing response
5. If no cache hit:
   - The primary LLM (Groq) is called
   - On failure, the system automatically falls back to Ollama
6. The response is stored in session memory and cache
7. The response is returned to the frontend

---

## Scope, Constraints, and Design Decisions

This project intentionally avoids over-engineering and sticks strictly to the stated objectives.

### What This Project Demonstrates Well

- Context-aware multi-turn conversation
- Automatic model fallback for reliability
- Practical system design with clear separation of components
- Cost-aware API usage through caching
- Robust behavior under failure conditions

### What This Project Is Not

❌ A production-ready chatbot  
- No authentication, rate limiting, monitoring, logging, or deployment hardening

❌ A custom-trained or fine-tuned LLM  
- Uses existing pre-trained models only

❌ A full Retrieval-Augmented Generation (RAG) system  
- No vector databases
- No embeddings
- No semantic document search

---

## Known Limitations

- Memory is session-based and non-persistent
- No database-backed long-term memory
- No cache TTL or eviction policies
- Cache is fully in-memory
- Ollama responses may be lower quality than cloud models
- Local inference requires sufficient system resources

These limitations are intentional and aligned with the project scope.

---

## How to Run the Project Locally

1. Activate the virtual environment  
   venv\Scripts\activate

2. Start the FastAPI server  
   python -m uvicorn app.main:app --reload

3. Open the application in a browser  
   http://127.0.0.1:8000

---

## Sample Test Prompts

- Hi
- My name is Arun
- What is my name?
- I have an exam tomorrow
- What subject is my exam for?
- What is 25 × 16?
- Ask the same question twice to observe caching
- Disconnect internet access to test Ollama fallback

---

## Demo Video

▶️ Watch the full working demo:  
[Click here to view the demo video](docs/demo.mp4)

(The demo showcases multi-turn memory, caching behavior, and fallback model activation.)

---

## Final Notes

This project prioritizes clarity, reliability, and correctness over unnecessary complexity.

All architectural and design choices were made deliberately to match the stated objectives and constraints, making the project suitable for academic evaluation and technical review.
