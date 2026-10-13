# PromptBridge — GenAI Conversational REST API

A FastAPI backend that takes a user message, validates it with Pydantic, sends it to the Gemini API, and returns a structured JSON response.

> Add a screenshot of the Swagger page (`/docs`) here: `![Demo](assets/demo.png)`

## Problem
Apps and frontends need a simple, reliable way to talk to an LLM without exposing API keys. PromptBridge acts as a small backend layer between a client and the Gemini API.

## How it works

```
Client ──POST /chatbot──► FastAPI ──► Pydantic validation ──► Gemini API
   ▲                                                              │
   └──────────────── JSON response / HTTP error ◄─────────────────┘
```

## Tech Stack
Python, FastAPI, Pydantic, Gemini API (`google-genai`), python-dotenv, Uvicorn

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Service status |
| GET | `/health` | Health check |
| POST | `/chatbot` | Send a message and get the Gemini response |
| GET | `/docs` | Interactive Swagger documentation |

**Request**
```json
{
  "message": "Explain REST APIs in simple words",
  "max_tokens": 512
}
```

**Response**
```json
{
  "response": "A REST API lets two programs talk over HTTP..."
}
```

## Features
- Request validation with Pydantic (`message`, optional `max_tokens`)
- API key loaded from environment variables (never hard-coded)
- `HTTPException` error handling with clear error messages
- Health-check endpoint
- Auto-generated API docs at `/docs`

## How to Run

1. Clone the repo
   ```bash
   git clone https://github.com/PravashisBiswal/FastApi-Using-Gemini.git
   cd FastApi-Using-Gemini
   ```
2. Install packages
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file (copy `.env.example`) and add your own key
   ```
   GEMINI_API_KEY=your_gemini_key
   ```
4. Start the server
   ```bash
   uvicorn Fast_Api_Using_Gemini:app --reload
   ```
5. Open `http://127.0.0.1:8000/docs` and try the `/chatbot` endpoint.

**Test with curl**
```bash
curl -X POST http://127.0.0.1:8000/chatbot \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
```

> Never commit your `.env` file or API keys.

## Future Improvements
- Chat history and session memory
- Streaming responses
- Rate limiting and API authentication
- Docker support and cloud deployment
- Automated tests with pytest

## Links
- Live Demo: [https://www.linkedin.com/posts/pravashisbiswal_generativeai-fastapi-python-activity-7514354770275364864-rZDN?utm_source=share&utm_medium=member_desktop&rcm=ACoAADkWWUYB5cnJ2PJLirJ_0r0TqPUtBV19K7w]

## Author
Pravashis Biswal — [LinkedIn](https://www.linkedin.com/in/pravashisbiswal) · [GitHub](https://github.com/pravashisbiswal)
