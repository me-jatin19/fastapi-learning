from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:4b"
)

def ask_llm(context, question):

    prompt = f"""
You are a helpful assistant.

Context:
{context}

Question:
{question}

Answer using only the context provided.
"""

    response = llm.invoke(prompt)

    return response.content