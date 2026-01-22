import os
import pdfplumber

def load_documents():
    documents = []

    # 🔑 Project root path
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "Data")  

    for file in os.listdir(data_dir):
        path = os.path.join(data_dir, file)

        if file.lower().endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                documents.append(f.read())

        elif file.lower().endswith(".pdf"):
            text = ""
            with pdfplumber.open(path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            documents.append(text)

    return documents
