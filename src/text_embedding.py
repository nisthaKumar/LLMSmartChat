from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize SentenceTransformer model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
batch_size = 2

def embed_chunks(chunks):
    logging.info(f"Starting embedding process for {len(chunks)} chunks.")
    
    # Generate embeddings for the chunks
    embeddings = embedding_model.encode(chunks, batch_size=batch_size, normalize_embeddings=True)
    logging.info(f"Generated embeddings for {len(chunks)} chunks. Embedding shape: {embeddings.shape}")

    return np.array(embeddings)

def build_faiss_index(embeddings):
    logging.info("Starting FAISS index creation.")
    
    # Determine the dimension of the embeddings
    dimension = embeddings.shape[1]
    logging.info(f"Embedding dimension: {dimension}")
    
    # Create the FAISS index
    index = faiss.IndexFlatL2(dimension)
    logging.info("FAISS index created successfully.")

    # Add embeddings to the FAISS index
    index.add(embeddings)
    logging.info(f"Added {embeddings.shape[0]} embeddings to the FAISS index.")

    return index
