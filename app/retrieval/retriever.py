from app.vectorstore.qdrant_db import vectorstore

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 5}
)

def retrieve(query):

    docs = retriever.invoke(query)

    return docs