import openai
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

openai.api_key = os.environ['OPENAI_API_KEY']

def generate_response(query, relevant_chunks):

    # Combine relevant chunks into a single context
    context = " ".join(relevant_chunks)
    logging.info("Context generated for the query.")

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Answer the question based on the context below:\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:\
                                    If the context is not present in the document, return Data Not Available as the response."}
    ]
    
    logging.info(f"Sending request to OpenAI API with the question: {query}")

    try:
        # Send request to OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  
            messages=messages,
            max_tokens=200,  
            temperature=0.7, 
            logprobs=True
        )
        
        # Extract the answer from the response
        answer = response['choices'][0]['message']['content'].strip()
        logging.info(f"Received answer from OpenAI: {answer}")
        
        # Extract logprobs if available
        logprobs = response['choices'][0].get('logprobs', {}).get('top_logprobs', [])
        logging.debug(f"Logprobs: {logprobs}")

        # Calculate confidence score based on logprobs
        avg_logprob = sum([sum(log) for log in logprobs]) / len(logprobs) if logprobs else 0
        confidence_score = max(avg_logprob, 0)
        logging.info(f"Calculated confidence score: {confidence_score}")

        low_confidence_threshold = -2.0  
        if confidence_score < low_confidence_threshold:
            logging.warning("Low confidence answer detected.")
            return "Low confidence answer detected."
        
        return answer

    except Exception as e:
        logging.error(f"Error with OpenAI API request: {e}")
        return "There was an error generating the answer. Please try again later."
