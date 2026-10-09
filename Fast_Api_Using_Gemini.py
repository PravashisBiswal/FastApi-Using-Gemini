from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

app = FastAPI(title="PromptBridge")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(
    api_key=api_key
)

class ChatRequest(BaseModel):
    message: str
    max_tokens: int = 1024

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "PromptBridge Created by Pravashis_biswal"
    }

@app.post("/chatbot")
def chatbot(req: ChatRequest):

    try:

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=req.message
        )

        return {
            "response": response.text
        }

    except Exception as e:

        print("GEMINI ERROR:", repr(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )