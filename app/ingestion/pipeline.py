from app.ingestion.loader import load_pdf
from app.ingestion.chunker import split_documents

from app.vectorstore.qdrant_db import vectorstore

def ingest_pdf(path):

    documents = load_pdf(path)

    chunks = split_documents(documents)

    vectorstore.add_documents(chunks)

    print("PDF ingested successfully")