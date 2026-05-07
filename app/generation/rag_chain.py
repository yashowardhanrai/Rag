from app.retrieval.retriever import retrieve
from app.generation.llm import llm

def ask_question(query):

    docs = retrieve(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are an expert AI assistant.

Answer ONLY from the provided context.

If answer not found say:
"I could not find this information."

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return response.content