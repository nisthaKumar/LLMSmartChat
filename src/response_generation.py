import openai
import os

openai.api_key = os.environ['openai_api_key']
def generate_response(query, relevant_chunks):

    context = " ".join(relevant_chunks)

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Answer the question based on the context below:\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  
            messages=messages,
            max_tokens=200,  
            temperature=0.7, 
            logprobs=True
        )
        
        answer = response['choices'][0]['message']['content'].strip()
        logprobs = response['choices'][0].get('logprobs', {}).get('top_logprobs', [])

        avg_logprob = sum([sum(log) for log in logprobs]) / len(logprobs) if logprobs else 0
        confidence_score = max(avg_logprob, 0)

        low_confidence_threshold = -2.0  
        if confidence_score < low_confidence_threshold:
            return "Low confidence answer detected."
        
        return answer

    except Exception as e:
        print(f"Error with OpenAI API request: {e}")
        return "There was an error generating the answer. Please try again later."
