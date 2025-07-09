from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def load_embedder():
    return SentenceTransformer(EMBEDDING_MODEL)