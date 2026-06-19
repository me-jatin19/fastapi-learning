from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:4b"
)

def ask_llm(history, context, question):

    prompt = f"""
Conversation History:
{history}

Context:
{context}

Question:
{question}

Answer using the conversation history and context.
"""

    response = llm.invoke(prompt)

    return response.content