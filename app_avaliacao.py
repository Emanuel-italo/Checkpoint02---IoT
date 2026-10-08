import os
from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from google.genai import types

# Chave e system prompt vêm de variáveis de ambiente (nunca escreva a chave no código)
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODELO = os.environ.get("MODELO_GEMINI", "gemini-3.5-flash-lite")
SYSTEM_PROMPT = os.environ.get("SYSTEM_PROMPT", "Você é um assistente prestativo.")

app = FastAPI()

# Histórico por sessão (já no formato do Gemini)
sessoes: dict[str, list] = {}

class Pergunta(BaseModel):
    session_id: str
    mensagem: str

@app.post("/chat")
def chat(pergunta: Pergunta):
    historico = sessoes.setdefault(pergunta.session_id, [])
    historico.append({"role": "user", "parts": [{"text": pergunta.mensagem}]})

    resposta = client.models.generate_content(
        model=MODELO,
        contents=historico,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            max_output_tokens=300,
        ),
    )
    texto = resposta.text

    historico.append({"role": "model", "parts": [{"text": texto}]})

    return {"session_id": pergunta.session_id, "resposta": texto}

@app.delete("/sessao/{session_id}")
def limpar_sessao(session_id: str):
    sessoes.pop(session_id, None)
    return {"status": "sessão apagada", "session_id": session_id}
