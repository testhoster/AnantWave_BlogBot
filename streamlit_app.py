import streamlit as st
from answer_quantum_question import answer_quantum_question

st.set_page_config(page_title="BlogBot@AnantWave", page_icon="🧠")
st.title("AnantWave Quantum Research Assistant 🧠")
st.markdown("Ask questions based on your uploaded quantum research documents.")

question = st.text_input("Enter your question:", placeholder="e.g., What are quantum gates?")

if question:
    with st.spinner("Retrieving relevant context and generating answer..."):
        answer, sources, context = answer_quantum_question(question)

    st.subheader("📘 Answer")
    st.markdown(answer)

    st.subheader("📂 Sources")
    for src in sources:
        st.code(src)

    with st.expander("📄 Context Used"):
        st.text(context)
