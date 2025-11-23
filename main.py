from typing import Optional
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai

app = FastAPI()

class Mensagem(BaseModel):
    texto: str

@app.get("/")
def root():
    return {"message": "API funcionando"}

#Inicia uma conexão direta entre o cliente Gemini quando o módulo é carregado
def get_api_key():
    chave = os.getenv("GEMINI_API_KEY")
    if not chave:
        raise Exception("Gemini não foi configurado. Defina GEMINI_API_KEY")
    return chave

@app.post("/mensagem")
def receber_mensagem(msg: Mensagem):
    api_key = get_api_key()
    client = genai.Client(api_key=api_key)

    prompt = msg.texto

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text_out = None
        if hasattr(response, "text") and response.text:
            text_out = response.text
        else:
            try:
                text_out=response.output[0].content[0].text
            except Exception:
                text_out = str(response)
        return {"resposta": text_out}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao chamar Gemini {e}")
    