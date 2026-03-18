from fastapi import FastAPI
from app.agents.retriever import retrieve
from app.agents.summarizer import summarize
from app.agents.verifier import verify
from app.agents.generator import generate

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Multi-Agent RAG Running"}

@app.get("/ask")
def ask(query: str):
    context = retrieve(query)
    summary = summarize(context)
    verification = verify(summary)
    final_answer = generate(summary + "\n\nVerification:\n" + verification)

    return {
        "query": query,
        "answer": final_answer,
        "verification": verification
    }