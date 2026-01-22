from load_documents import load_documents

docs = load_documents()

print("Documents Loaded:", len(docs))
print(docs[0][:1000])
