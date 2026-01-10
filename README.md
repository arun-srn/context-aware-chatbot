                                        Context-Aware Chatbot with Memory and Fallback Models

A) Overview -
This project is a context-aware conversational chatbot built using FastAPI.
It is designed to handle multi-turn conversations, remember past interactions within a session, and remain functional even when the primary language model fails by automatically falling back to a local model.

The focus of this project is system design and reliability, not training models from scratch.

B) Key Features -
1. Multi-Turn Conversation Memory 

The chatbot maintains session-based memory.
Previous user and assistant messages are included in future prompts.
This allows the bot to respond consistently and contextually across multiple turns.
Memory is implemented in-memory for simplicity and performance.

2. Primary + Fallback Model Architecture 

Primary model: Groq-hosted LLM (fast, low-latency, cloud-based)
Fallback model: Locally hosted Ollama model
If the primary model: fails OR times out OR returns an error, the system automatically switches to Ollama without breaking the user experience.

3. Basic Context Retrieval

Relevant past messages from the same session are retrieved and appended to the prompt.
This ensures responses remain aligned with earlier conversation turns.
This project uses prompt-level retrieval, not embedding-based vector search, which is sufficient for short conversational memory as required by the problem statement.

4. Caching for Faster Responses

Frequently repeated user queries are cached in memory.
Cached responses are returned instantly, reducing: API calls, latency and cost.

5. Simple Web Interface

Lightweight HTML frontend
User messages are right-aligned
Assistant messages are left-aligned
Clean, chat-style interaction similar to common messaging apps

C) System Architecture (High Level)
User → FastAPI Backend

        ├── Cache (fast return if hit)

        ├── Primary LLM (Groq)

        │       └── on failure →

        └── Fallback LLM (Ollama)

D) Project Constraints & Design Decisions

This project intentionally does not over-engineer beyond the requirements.

1) Long-Term Memory -
Persistent long-term memory (database, embeddings, disk storage) is not implemented.
Reason: The problem statement does not require persistence across restarts, and adding it would increase complexity without clear benefit.

2) Cache Eviction / TTL -
Cache does not include TTL or eviction policies.
Reason: The scope focuses on demonstrating caching behavior, not production-grade cache management.

3) Retrieval-Augmented Generation (RAG) -
No vector database or embeddings are used.
Reason: The requirement is context awareness, not semantic document retrieval.

E) Tech Stack -

Backend: FastAPI (Python)
Primary LLM: Groq API
Fallback LLM: Ollama (local)
HTTP Client: httpx
Frontend: HTML + minimal JavaScript
Environment Management: dotenv

How to Run
# Activate virtual environment
venv\Scripts\Activate.ps1

# Start server
python -m uvicorn app.main:app --reload

Then open: http://127.0.0.1:8000

What This Project Demonstrates Well

✅ Context-aware conversation

✅ Model fallback reliability

✅ Practical system design

✅ Cost-aware API usage

✅ Clean separation of components


What This Project Is Not

❌ A production-ready chatbot

❌ A custom-trained LLM

❌ A full RAG system with embeddings

Final Notes -

This project prioritizes clarity, reliability, and alignment with requirements over unnecessary complexity.
All design choices were made deliberately to match the stated objectives and constraints.