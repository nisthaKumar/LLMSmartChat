from text_embedding import embedding_model
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def retrieve_relevant_chunks(query, index, chunks, top_k=3):
    logging.info(f"Retrieving relevant chunks for query: {query}")
    
    # Generate embedding for the query
    query_embedding = embedding_model.encode([query])
    logging.info(f"Query embedding generated. Shape: {query_embedding.shape}")
    
    # Perform the search in the FAISS index
    logging.info(f"Searching for top {top_k} relevant chunks in the FAISS index.")
    distances, indices = index.search(query_embedding, top_k)
    
    logging.info(f"Search complete. Found top {top_k} relevant chunks.")
    logging.debug(f"Indices of relevant chunks: {indices[0]}")
    
    # Return the relevant chunks based on the indices
    return [chunks[i] for i in indices[0]]
