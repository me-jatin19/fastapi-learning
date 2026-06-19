from fastapi import FastAPI
from pydantic import BaseModel

from rag_service import retrieve_context
from llm_service import ask_llm
from memory import add_message, get_history

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/chat")
def chat(request: QueryRequest):

    history = get_history()

    context = retrieve_context(
        request.question
    )

    answer = ask_llm(
        history,
        context,
        request.question
    )

    add_message(
        "user",
        request.question
    )

    add_message(
        "assistant",
        answer
    )

    return {
        "history": history,
        "answer": answer
    }