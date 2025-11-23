# Agente Inteligente Gemini 🚀

## Descrição do Projeto
Este projeto é uma **API em FastAPI** que integra **Inteligência Artificial (IA) com LLM (Gemini)**.  
Ela permite receber mensagens em texto e retornar **respostas inteligentes e estruturadas**, servindo como base para:

- Assistentes pessoais
- Análise de dados textuais
- Geração de insights automatizados

O projeto foi desenvolvido como **demonstração prática de habilidades em IA, APIs e integração com modelos de linguagem**, ideal para portfólio ou entrevistas de estágio.

---

## Funcionalidades

### ✅ Endpoint GET `/`
- Testa se a API está online
- Retorna confirmação de funcionamento
- Exemplo de resposta:
```json
{"message": "API funcionando"}
✅ Endpoint POST /mensagem
Recebe um JSON com texto

Retorna a resposta do modelo Gemini

Permite simular assistentes ou análises de texto

Exemplo de entrada:

json
Copiar código
{"texto": "Oi, como você está?"}
Exemplo de saída:

json
Copiar código
{"resposta": "Você enviou: Oi, como você está?"}

## Tecnologias e Aprendizado 
Python 3.14 – linguagem principal

FastAPI – criação de API rápida e interativa

Pydantic – validação de dados e tipagem

Uvicorn – servidor ASGI

Google Gemini (LLM) – geração de linguagem natural e insights

Git e GitHub – versionamento seguro do código

## Habilidades desenvolvidas
Criar e documentar API RESTful

Integrar IA em sistemas web

Trabalhar com variáveis de ambiente para segurança

Testar endpoints usando Swagger

Preparar projeto pronto para portfólio ou apresentação

Segurança e Boas Práticas
A chave da API Gemini nunca é armazenada no código

Uso de variáveis de ambiente para manter segredo

Estrutura do projeto preparada para GitHub sem risco de exposição

Como Rodar
Clonar repositório:

bash
Copiar código
git clone https://github.com/SEU_USUARIO/agente_ia_gemini.git
cd agente_ia_gemini
Criar e ativar ambiente virtual:

bash
Copiar código
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
Instalar dependências:

bash
Copiar código
pip install -r requirements.txt
Configurar variável de ambiente:

bash
Copiar código
# Windows PowerShell
setx Gemini_API_KEY "SUA_CHAVE_AQUI"
# Linux/macOS
export Gemini_API_KEY="SUA_CHAVE_AQUI"
Executar API:

bash
Copiar código
python -m uvicorn main:app --reload
Abrir Swagger:

arduino
Copiar código
http://127.0.0.1:8000/docs
Estrutura do Projeto
bash
Copiar código
agente_ia_gemini/
├─ main.py           # Código principal da API
├─ .venv/            # Ambiente virtual (não commitado)
├─ README.md         # Este arquivo
└─ requirements.txt  # Dependências