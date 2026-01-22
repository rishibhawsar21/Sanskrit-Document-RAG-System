import faiss
import numpy as np
import os
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

# ----- PATH FIX (IMPORTANT) -----
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAISS_INDEX_PATH = os.path.join(BASE_DIR, "faiss.index")
CHUNKS_PATH = os.path.join(BASE_DIR, "chunks.txt")

# Load FAISS index
index = faiss.read_index(FAISS_INDEX_PATH)

# Load chunks
with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
    chunks = f.readlines()

def retrieve_context(query, top_k=3):
    query_embedding = model.encode([query]).astype("float32")
    distances, indices = index.search(query_embedding, top_k)

    context = ""
    for idx in indices[0]:
        context += chunks[idx]

    return context
