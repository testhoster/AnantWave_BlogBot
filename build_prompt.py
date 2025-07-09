def build_prompt(context, question):
    if context.strip() and context != "No relevant context available.":
        return f"""
You are an expert assistant in Quantum Computing, Quantum Machine Learning, and related technologies.
You MUST ONLY answer based on the context below. If the context doesn't help, strictly say: 
"The provided documents do not contain information on this topic."

Context:
{context}

Question: {question}

Answer:
"""
    else:
        return f"""
You are an expert assistant in Quantum Computing.
The answer to the question is not found in the provided documents.

Question: {question}

Answer:
The provided documents do not contain information on this topic.
"""