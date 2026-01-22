from retriever import retrieve_context
from generator import generate_answer

query = input("प्रश्न लिखें: ")

context = retrieve_context(query)
answer = generate_answer(query, context)

print("\n📜 उत्तर:\n")
print(answer)
