# Context-Aware Chatbot with Memory and Fallback Models

## Project Overview

This project implements a context-aware conversational chatbot that can maintain awareness of past interactions and respond coherently across multiple conversation turns.

The chatbot uses an external large language model as the primary response generator and automatically falls back to a locally hosted model when the primary model is unavailable. The system also incorporates conversation memory and caching to improve reliability, consistency, and performance.

The goal of this project is to demonstrate practical system design for conversational AI rather than training or fine-tuning language models.

---

## Key Features

### 1. Multi-Turn Conversation Memory
- Maintains session-based chat history
- Previous user and assistant messages are included in each new prompt
- Enables coherent follow-up questions and context-aware responses

### 2. Primary and Fallback Model Support
- Primary model: Groq-hosted LLM (cloud-based)
- Fallback model: Ollama (locally hosted)
- Automatic fallback is triggered if the primary model fails due to API errors, quota limits, or network issues

### 3. Lightweight Context Retrieval
- Relevant past conversation turns are retrieved from stored session history
- Retrieved messages are appended directly to the prompt
- No embeddings or vector databases are used

### 4. Response Caching
- Frequently repeated user queries are cached in memory
- Cached responses are returned instantly when available
- Reduces latency and avoids unnecessary API calls

### 5. Simple Chat Interface
- Browser-based frontend using HTML, CSS, and JavaScript
- User messages are right-aligned
- Bot responses are left-aligned
- Designed to resemble common chat applications

---

## System Architecture (High Level)

User (Browser)  
→ FastAPI Backend  
→ LLM Router  
→ Primary LLM (Groq)  
→ Fallback LLM (Ollama)  
→ Memory + Cache  

---

## Technologies Used

- Backend: FastAPI (Python)
- Frontend: HTML, CSS, JavaScript
- Primary LLM: Groq API
- Fallback LLM: Ollama (local inference)
- HTTP Client: httpx
- Environment Variables: python-dotenv

---

## How the System Works

1. User sends a message through the browser
2. The backend receives the message along with a session ID
3. Past conversation history for that session is retrieved
4. Cache is checked for an existing response
5. If not cached:
   - The primary LLM (Groq) is called
   - If it fails, the system falls back to Ollama
6. The response is stored in memory and cache
7. The response is returned to the frontend

---

## Scope and Constraints

### What This Project Does
- Supports text-based conversations
- Maintains short-term conversational memory
- Uses existing pre-trained language models
- Provides automatic fallback for reliability
- Uses caching to optimize performance and cost

### What This Project Is Not

❌ A production-ready chatbot  
- No authentication, rate limiting, monitoring, or deployment hardening

❌ A custom-trained LLM  
- No model training or fine-tuning is performed

❌ A full RAG system with embeddings  
- No vector databases or semantic search
- Context retrieval is prompt-based only

---

## Known Limitations

- Memory is session-based and lightweight
- No TTL, eviction policies, or advanced cache persistence
- Long-term memory is not knowledge-based
- Fallback models may produce lower-quality responses
- Ollama requires sufficient local system resources

These limitations are intentional and aligned with the project scope.

---

## How to Run the Project Locally

1. Activate the virtual environment  
   venv\Scripts\activate

2. Start the backend server  
   python -m uvicorn app.main:app --reload

3. Open the application in a browser  
   http://127.0.0.1:8000

---

## Sample Test Prompts

- Hi
- My name is Arun
- What is my name?
- I have my Calculus exam tomorrow
- What subject is my exam for?
- What is 25 × 16?
- Ask the same question twice to observe caching
- Disconnect internet to test Ollama fallback

---

## Conclusion

This project demonstrates a practical implementation of a context-aware chatbot with memory, fallback mechanisms, and caching.

It focuses on system design, robustness, and real-world engineering trade-offs rather than model training, making it suitable for academic evaluation and technical review.
