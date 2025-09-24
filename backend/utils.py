import openai
from config import OPENAI_API_KEY, MODEL_NAME

openai.api_key = OPENAI_API_KEY

def get_gpt_response(user_input):
    try:
        response = openai.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are an AI companion for learners."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error calling GPT: {e}"

def log_query(user_input, response):
    with open("chat_log.txt", "a", encoding="utf-8") as f:
        f.write(f"User: {user_input}\nAI: {response}\n\n")
