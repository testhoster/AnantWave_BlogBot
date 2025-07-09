import faiss
import pickle

FAISS_INDEX_PATH = "./faiss_index.idx"
METADATA_PATH = "./metadata.pkl"

def load_faiss_index_and_metadata():
    index = faiss.read_index(FAISS_INDEX_PATH)
    with open(METADATA_PATH, "rb") as f:
        metadata = pickle.load(f)
    return index, metadata