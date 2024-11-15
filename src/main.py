import sys
import json
from pdf_processor import read_and_process_pdf
from text_embedding import embed_chunks, build_faiss_index
from retrieval import retrieve_relevant_chunks
from response_generation import generate_response

def main(pdf_path, questions):

    pdf_chunks = read_and_process_pdf(pdf_path)
    embeddings = embed_chunks(pdf_chunks)
    index = build_faiss_index(embeddings)

    results = {}
    for question in questions:
        relevant_chunks = retrieve_relevant_chunks(question, index, pdf_chunks)
        answer = generate_response(question, relevant_chunks)
        results[question] = answer

    return json.dumps(results)

# Example usage
if __name__ == "__main__":

    pdf_path = sys.argv[1]  
    questions = sys.argv[2:]
   
    output = main(pdf_path, questions)
    print(output)
