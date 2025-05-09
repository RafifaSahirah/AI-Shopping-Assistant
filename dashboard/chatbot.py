import time
import openai
from config import OPENAI_API_KEY, BASE_URL

client = openai.Client(api_key=OPENAI_API_KEY, base_url=BASE_URL)

def chatbot_response(user_query):
    """Generate AI-powered shopping assistant response with OpenAI API."""
    for attempt in range(3):  
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  
                messages=[{"role": "user", "content": user_query}],
                max_tokens=300,  # Increase token limit
                temperature=0.3,
                stop=None
            )
            if response.choices:
                return response.choices[0].message.content.strip()

        except openai.OpenAIError as e:
            if "rate limit" in str(e).lower():
                wait_time = 10 * (attempt + 1)
                print(f"Rate limit exceeded, retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print(f"OpenAI API error: {e}")
                break

    return "Sorry, the AI response is incomplete or unavailable. Please try again."
