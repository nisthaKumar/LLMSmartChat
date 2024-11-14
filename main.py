# main.py
import sys
from pdf_processor import read_and_process_pdf
from text_embedding import embed_chunks, build_faiss_index
from retrieval import retrieve_relevant_chunks
from answer_generation import generate_answer

def main(pdf_path, question):
    pdf_chunks = read_and_process_pdf(pdf_path)

    embeddings = embed_chunks(pdf_chunks)

    index = build_faiss_index(embeddings)

    # # Step 4: Retrieve relevant chunks
    relevant_chunks = retrieve_relevant_chunks(question, index, pdf_chunks)

    # # Step 5: Generate and return the answer
    answer = generate_answer(question, relevant_chunks)
    return answer

# Example usage
if __name__ == "__main__":
    pdf_path = sys.argv[1]  # Path to your PDF file
    questions = ["What is the name of the company?", 
                "Who is the CEO of the company?",
                # "What is their vacation policy?",
                # "What is the termination policy?",
                "How many employees are there in this company?"]
    #questions = sys.argv[2]
    for question in questions:
        answer = main(pdf_path, question)
        print("Answer:", answer)
