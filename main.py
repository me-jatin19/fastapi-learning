from fastapi import FastAPI
from pydantic import BaseModel

from rag_service import retrieve_context
from llm_service import ask_llm

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/chat")
def chat(request: QueryRequest):

    context = retrieve_context(
        request.question
    )

    answer = ask_llm(
        context,
        request.question
    )

    return {
        "question": request.question,
        "answer": answer
    }