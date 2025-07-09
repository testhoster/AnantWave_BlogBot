import numpy as np
from embedder_loader import load_embedder
from faiss_loader import load_faiss_index_and_metadata
from build_prompt import build_prompt
from generate_with_ollama import generate_with_ollama

FAISS_THRESHOLD = 1.0
MAX_CONTEXT_CHUNKS = 5

embedder = load_embedder()
index, metadata = load_faiss_index_and_metadata()

def answer_quantum_question(user_question, top_k=5):
    query_embedding = embedder.encode([user_question])[0].astype(np.float32).reshape(1, -1)
    D, I = index.search(query_embedding, k=top_k)

    context_chunks = []
    sources = []

    for dist, idx in zip(D[0], I[0]):
        if idx < len(metadata) and dist < FAISS_THRESHOLD:
            item = metadata[idx]
            content = item.get("content", "")
            if content.strip():
                context_chunks.append(content)
                sources.append(item.get("source", f"doc_{idx}"))

    context_chunks = context_chunks[:MAX_CONTEXT_CHUNKS]
    context_text = "\n".join(context_chunks) if context_chunks else "No relevant context available."
    sources = list(set(sources)) or ["No relevant sources found."]

    prompt = build_prompt(context_text, user_question)
    answer = generate_with_ollama(prompt)

    return answer, sources, context_text
