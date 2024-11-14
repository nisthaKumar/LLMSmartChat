from text_embedding import embedding_model

def retrieve_relevant_chunks(query, index, chunks, top_k=3):
    query_embedding = embedding_model.encode([query])
    _, indices = index.search(query_embedding, top_k)
    return [chunks[i] for i in indices[0]]
