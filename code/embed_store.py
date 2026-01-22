import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from load_documents import load_documents
from preprocess import clean_text, chunk_text

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

def build_faiss_index():
    docs = load_documents()
    all_chunks = []

    for doc in docs:
        cleaned = clean_text(doc)
        chunks = chunk_text(cleaned)
        all_chunks.extend(chunks)

    embeddings = model.encode(all_chunks)
    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, "faiss.index")

    with open("chunks.txt", "w", encoding="utf-8") as f:
        for chunk in all_chunks:
            f.write(chunk + "\n")

    print("✅ FAISS index built successfully")

if __name__ == "__main__":
    build_faiss_index()
