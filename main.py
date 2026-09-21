OLLAMA_BASE_URL = "http://localhost:11434/v1"

from openai import OpenAI

ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')

response = ollama.chat.completions.create(model="llama3.2", messages=[{"role": "user", "content": "Tell me a dad joke."}])

print(response.choices[0].message.content)
