from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_KEY:
    raise RuntimeError("OPEN_API_KEY no encontrado en .env")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Memoria que guarda los ultimos 10 mensajes
conversation_history = []
MAX_HISTORY = 10

class ChatRequest(BaseModel):
    text: str

@app.post("/chat")
async def chat_endpoint(body: ChatRequest):
    try:

        user_message = body.text

        # Agregar mensaje del user a la memoria
        conversation_history.append({"role": "user", "content": user_message})

        # Limitar el historial
        if len(conversation_history) > MAX_HISTORY:
            del conversation_history[0]

        # Construcción de mensajes completos para el modelo

        messages=[
            {"role": "system", 
             "content": "Eres un médico con mucha experiencia que responde claro, con advertencias y siempre sugiere consultar a un profesional. Mantén respuestas consisas."},
            {"role": "user", "content": body.text}
        ] + conversation_history

        # Llamada al modelo

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=300,
            temperature=0.3
        )

        reply = response.choices[0].message.content

        # Guardar también respuesta del asistente
        conversation_history.append({"role": "assistant", "content": reply})

        if len(conversation_history) > MAX_HISTORY:
            del conversation_history[0]
        
        return {"reply": reply}

    except Exception as e:
        raise HTTPException(status_code=500, details=str(e))

