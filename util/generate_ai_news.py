import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("openai_api_key")


def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em marketing bancário.",
            },
            {
                "role": "user",
                "content": f"""Crie uma mensagem para {user['name']}
          sobre a importância dos investimentos (máximo de 100 caracteres)""",
            },
        ],
    )
    return completion.choices[0].message.content.strip('"')
