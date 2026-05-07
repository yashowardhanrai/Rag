import sys
import os

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, project_root)

import streamlit as st

from app.ingestion.pipeline import ingest_pdf
from app.generation.rag_chain import ask_question


st.set_page_config(
    page_title="Advanced RAG System",
    layout="wide"
)

st.title("📚 Advanced RAG System")

st.write("Upload a PDF and ask questions.")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file is not None:

    # Save uploaded PDF
    pdf_path = f"data/{uploaded_file.name}"

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully!")

    # Process PDF
    with st.spinner("Processing PDF..."):

        ingest_pdf(pdf_path)

    st.success("PDF processed successfully!")

query = st.text_input("Ask Question")

if st.button("Submit"):

    if query:

        with st.spinner("Generating answer..."):

            response = ask_question(query)

        st.write("## Answer")

        st.write(response)