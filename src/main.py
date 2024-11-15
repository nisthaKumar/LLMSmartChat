import sys
import json
import logging
from pdf_processor import read_and_process_pdf
from text_embedding import embed_chunks, build_faiss_index
from retriever import retrieve_relevant_chunks
from response_generator import generate_response

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main(pdf_path, questions):
    logging.info("Starting PDF processing")
    
    # Read and process the PDF
    pdf_chunks = read_and_process_pdf(pdf_path)
    logging.info(f"Processed PDF into {len(pdf_chunks)} chunks")

    # Embed the chunks
    embeddings = embed_chunks(pdf_chunks)
    logging.info(f"Generated embeddings for {len(embeddings)} chunks")

    # Build FAISS index
    index = build_faiss_index(embeddings)
    logging.info("FAISS index built successfully")

    results = {}
    for question in questions:
        logging.info(f"Processing question: {question}")

        # Retrieve relevant chunks based on the question
        relevant_chunks = retrieve_relevant_chunks(question, index, pdf_chunks)
        logging.info(f"Retrieved {len(relevant_chunks)} relevant chunks for the question")

        # Generate the response
        answer = generate_response(question, relevant_chunks)
        logging.info(f"Generated response for question: {question}")

        results[question] = answer

    logging.info("All questions processed successfully")
    return results

# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 3:
        logging.error("Invalid number of arguments. \nUsage: python script.py <pdf_path> <question1> <question2> ...")
        sys.exit(1)

    try:
        pdf_path = sys.argv[1]  
        questions = sys.argv[2:]
        logging.info(f"PDF path: {pdf_path}")
        logging.info(f"Questions: {questions}")
   
        results = main(pdf_path, questions)

        # Modified output: formatted JSON with question-answer pairs
        output = {
            "status": "success",
            "total_questions": len(questions),
            "questions_and_answers": [{"question": question, "answer": answer} for question, answer in results.items()]
        }
        

        # Output in JSON format
        print("\nFormatted JSON output:")
        print(json.dumps(output, indent=4))

        # Write to a file
        with open("output.json", "w") as output_file:
            json.dump(output, output_file, indent=4)

        logging.info("Processing complete. Results written to output.json.")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        sys.exit(1)
