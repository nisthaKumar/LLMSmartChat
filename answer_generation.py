import openai
import os

# Optionally load the API key from environment variables for security
openai.api_key = os.environ['OPENAI_API_KEY']
def generate_answer(query, relevant_chunks):
    # Combine the relevant chunks into a single context
    context = " ".join(relevant_chunks)

    # Set up the chat messages for the GPT-4 API
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Answer the question based on the context below:\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"}
    ]

    # Call the OpenAI API to get the answer
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Make sure you have access to GPT-4
            messages=messages,
            max_tokens=200,  # Set max tokens for the response
            temperature=0.7,  # Control randomness in output (0 for deterministic)
            logprobs=True
        )
        
        # Extract and return the generated answer
        answer = response['choices'][0]['message']['content'].strip()
        logprobs = response['choices'][0].get('logprobs', {}).get('top_logprobs', [])

        avg_logprob = sum([sum(log) for log in logprobs]) / len(logprobs) if logprobs else 0
        confidence_score = max(avg_logprob, 0)

        low_confidence_threshold = -2.0  # This can be adjusted based on empirical results
        if confidence_score < low_confidence_threshold:
            return "Low confidence answer detected."
        
        return answer

    except Exception as e:
        print(f"Error with OpenAI API request: {e}")
        return "There was an error generating the answer. Please try again later."
