# Sanskrit Document Retrieval-Augmented Generation (RAG) System

A complete **CPU-only Retrieval-Augmented Generation (RAG)** system for querying **Sanskrit documents (PDF/Text)**.  
This project ingests Sanskrit documents, retrieves relevant context using semantic search, and provides grounded answers through a lightweight and resource-efficient approach.  
It also includes an interactive **Streamlit UI** and is **deployable on Render**.

---

## 📌 Objective

The objective of this project is to:

- Build an **end-to-end RAG pipeline** for Sanskrit documents
- Ensure **CPU-only inference** (no GPU usage)
- Support **Sanskrit PDF/Text ingestion**
- Retrieve semantically relevant context using FAISS
- Generate **grounded answers** with minimal resource usage
- Provide a **user-friendly Streamlit interface**
- Make the project **GitHub-ready and cloud-deployable**

---

## 🏗️ System Architecture

Sanskrit PDF / Text
↓
Document Loader (pdfplumber)
↓
Text Cleaning & Chunking
↓
Embedding Generation (Sentence Transformers)
↓
Vector Indexing (FAISS – CPU)
↓
Query Embedding
↓
Top-K Context Retrieval
↓
Lightweight Generator (Extractive RAG)
↓
Final Answer

---

## 🧰 Tech Stack

| Component | Technology |
|--------|-----------|
| Programming Language | Python 3.10+ |
| PDF Processing | pdfplumber |
| Embeddings | sentence-transformers (multilingual) |
| Vector Search | FAISS (CPU) |
| Generator | Extractive (context-grounded) |
| UI | Streamlit |
| Deployment | Render |
| Hardware | CPU only |

--

## 📁 Project Structure

Sanskrit-Document-RAG-System/
│
├── app.py # Streamlit UI
│
├── code/
│ ├── __init__.py
│ ├── embed_store.py # Build FAISS index
│ ├── retriever.py # Context retrieval
│ ├── generator.py # Lightweight generator
│ ├── load_documents.py # PDF/Text loader
│ ├── preprocess.py # Cleaning & chunking
│ └── main.py # CLI entry point
│
├── Data/
│ └── Sanskrit_docs.pdf # Provided Sanskrit document
│
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
└── (Generated locally)
├── faiss.index # Vector index (not pushed)
└── chunks.txt # Chunk mapping (not pushed)

## ▶️ How to Run

```bash
pip install -r requirements.txt
python code/embed_store.py
streamlit run app.py
