from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

from langchain_qdrant import QdrantVectorStore

from app.vectorstore.embedding import embedding_model

client = QdrantClient(
    path="qdrant_data"
)

# Create collection if not exists
try:
    client.get_collection("rag_collection")

except:
    client.create_collection(
        collection_name="rag_collection",
        vectors_config=VectorParams(
            size=1024,
            distance=Distance.COSINE
        )
    )

vectorstore = QdrantVectorStore(
    client=client,
    collection_name="rag_collection",
    embedding=embedding_model
)