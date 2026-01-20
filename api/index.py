from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# CORS so the frontend can talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/api/chat")
def chat(request: ChatRequest):
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY not configured")
    
    try:
        user_message = request.message

        # System prompt to enforce clear, well-structured, markdown-formatted responses
        system_prompt = (
            "You are a supportive mental coach specializing in mental health, stress management, motivation, "
            "habit formation, confidence building, and emotional well-being.\n\n"
            
            "**Handling Unrelated Questions:**\n"
            "If a user asks a question that is unrelated to mental health, coaching, or emotional well-being "
            "(e.g., general knowledge, math problems, coding, cooking recipes, etc.), you must:\n"
            "1. Politely decline to answer the question\n"
            "2. Clearly state your purpose and expertise as a mental health coach\n"
            "3. Provide 3-5 example questions the user can ask related to mental health\n\n"
            
            "**Response Format:**\n"
            "Always respond in **GitHub-flavored Markdown** with:\n"
            "- A clear top-level heading summarizing the response\n"
            "- Short introductory paragraph\n"
            "- Subheadings (###) for key sections\n"
            "- Bullet lists for strategies, options, or steps\n"
            "- Numbered lists for ordered action plans\n"
            "- Short paragraphs (2–4 sentences) instead of long walls of text\n"
            "- Occasional bolding for key ideas, but do not overuse it\n\n"
            
            "Keep the tone warm, practical, and non-clinical. Avoid using emojis unless the user uses them first. "
            "Never include Markdown code fences (```), HTML, or JSON in your replies—only regular Markdown headings, lists, and text."
        )

        response = client.chat.completions.create(
            model="gpt-5",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )
        return {"reply": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calling OpenAI API: {str(e)}")
