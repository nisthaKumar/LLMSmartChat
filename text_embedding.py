from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
batch_size = 2

def embed_chunks(chunks):
    embeddings = embedding_model.encode(chunks, batch_size=batch_size, normalize_embeddings=True)
    return np.array(embeddings)

def build_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index
