# Advanced RAG System

An advanced Retrieval-Augmented Generation (RAG) application built using:

- LangChain
- Streamlit
- Qdrant
- Groq LLMs
- HuggingFace Embeddings

This project allows users to upload PDF documents and ask questions based on the document content using an AI-powered chatbot.

---

# Features

- PDF Upload
- Semantic Search
- Vector Database Storage
- AI Question Answering
- Streamlit Frontend
- Local Qdrant Vector Store
- Open Source Embeddings
- Groq LLM Integration
- Fast Retrieval Pipeline

---

# Tech Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| LLM | Llama 3.3 70B (Groq) |
| Embeddings | sentence-transformers/all-MiniLM-L6-v2 |
| Vector Database | Qdrant |
| Framework | LangChain |
| Language | Python |

---

# Project Structure

```bash
advanced-rag/
│
├── app/
│   ├── ingestion/
│   ├── retrieval/
│   ├── generation/
│   ├── vectorstore/
│   └── utils/
│
├── frontend/
│   └── streamlit_app.py
│
├── data/
├── qdrant_data/
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd advanced-rag
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from:

https://console.groq.com/

---

# Run the Project

```bash
streamlit run frontend/streamlit_app.py
```

---

# How It Works

```text
PDF Upload
    ↓
Document Chunking
    ↓
Embedding Generation
    ↓
Qdrant Vector Storage
    ↓
Semantic Retrieval
    ↓
LLM Response Generation
    ↓
Answer Display
```

---

# Example Questions

- What is this document about?
- Summarize the PDF
- Explain the main concepts
- What are the key findings?

---

# Embedding Model

```python
sentence-transformers/all-MiniLM-L6-v2
```

---

# LLM Used

```python
llama-3.3-70b-versatile
```

Provided by Groq.

---

# Future Improvements

- Chat Memory
- Multi-PDF Support
- Hybrid Search
- Reranking
- Citations
- Authentication
- Docker Deployment
- Agentic RAG
- Multimodal Support

---

# Author

Yashowardhan Rai
