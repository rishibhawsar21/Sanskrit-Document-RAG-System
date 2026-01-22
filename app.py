import streamlit as st
from code.retriever import retrieve_context
from code.generator import generate_answer

st.set_page_config(
    page_title="Sanskrit Document RAG System",
    layout="centered"
)

st.title("🕉️ Sanskrit Document RAG System")
st.markdown(
    "Ask questions based on the provided Sanskrit documents (PDF/Text). "
    "This system runs fully on **CPU-only**."
)

st.divider()

# Input query
query = st.text_input(
    "📜 Enter your Sanskrit question:",
    placeholder="उदाहरण: शंखनादः किम् करोति?"
)

# Button
if st.button("🔍 Get Answer"):
    if not query.strip():
        st.warning("कृपया प्रश्न लिखें।")
    else:
        with st.spinner("Searching documents and generating answer..."):
            context = retrieve_context(query)
            answer = generate_answer(query, context)

        st.subheader("✅ Answer")
        st.write(answer)

        with st.expander("📂 Retrieved Context"):
            st.write(context)
