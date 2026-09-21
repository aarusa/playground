import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")

if not OLLAMA_BASE_URL:
    raise ValueError("OLLAMA_BASE_URL is not set in the .env file or environment variables.")

# Initialize OpenAI client pointing to Ollama
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')

DEFAULT_MODEL = "llama3.2"

system_prompt = """
You are a ghost that takes a technical question and responds with a spooky explanation in one line.
"""

user_prompt = input("Ask: ")

def create_message():
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]


# print(create_message())

response = ollama.chat.completions.create(
    model=DEFAULT_MODEL,
    messages=create_message()
)

print(response.choices[0].message.content)

# response = ollama.chat.completions.create(DEFAULT_MODEL, messages=create_message())
# print(response.choices[0].message.content)