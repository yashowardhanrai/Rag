from app.ingestion.pipeline import ingest_pdf

from app.generation.rag_chain import ask_question

pdf_path = "data/sample.pdf"

ingest_pdf(pdf_path)

while True:

    query = input("\nAsk Question: ")

    if query == "exit":
        break

    answer = ask_question(query)

    print("\nAnswer:\n")

    print(answer)