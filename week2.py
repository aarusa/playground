import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

# importing api keys from .env
load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')
deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')
grok_api_key = os.getenv('GROK_API_KEY')
openrouter_api_key = os.getenv('OPENROUTER_API_KEY')

# check if api keys exists
# if openai_api_key:
#     print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
# else:
#     print("OpenAI API Key not set")
    
# if anthropic_api_key:
#     print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
# else:
#     print("Anthropic API Key not set (and this is optional)")

# if google_api_key:
#     print(f"Google API Key exists and begins {google_api_key[:2]}")
# else:
#     print("Google API Key not set (and this is optional)")

# if deepseek_api_key:
#     print(f"DeepSeek API Key exists and begins {deepseek_api_key[:3]}")
# else:
#     print("DeepSeek API Key not set (and this is optional)")

# if groq_api_key:
#     print(f"Groq API Key exists and begins {groq_api_key[:4]}")
# else:
#     print("Groq API Key not set (and this is optional)")

# if grok_api_key:
#     print(f"Grok API Key exists and begins {grok_api_key[:4]}")
# else:
#     print("Grok API Key not set (and this is optional)")

# if openrouter_api_key:
#     print(f"OpenRouter API Key exists and begins {openrouter_api_key[:3]}")
# else:
#     print("OpenRouter API Key not set (and this is optional)")


# connect to OpenAI client library

openai = OpenAI()

anthropic_url = "https://api.anthropic.com/v1/"
gemini_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
deepseek_url = "https://api.deepseek.com"
groq_url = "https://api.groq.com/openai/v1"
grok_url = "https://api.x.ai/v1"
openrouter_url = "https://openrouter.ai/api/v1"
ollama_url = "http://localhost:11434/v1"

anthropic = OpenAI(api_key=anthropic_api_key, base_url=anthropic_url)
gemini = OpenAI(api_key=google_api_key, base_url=gemini_url)
deepseek = OpenAI(api_key=deepseek_api_key, base_url=deepseek_url)
groq = OpenAI(api_key=groq_api_key, base_url=groq_url)
grok = OpenAI(api_key=grok_api_key, base_url=grok_url)
openrouter = OpenAI(base_url=openrouter_url, api_key=openrouter_api_key)
ollama = OpenAI(api_key="ollama", base_url=ollama_url)

tell_a_joke = [
    {"role": "user", "content": "Tell a joke for a student on the journey to becoming an expert in LLM Engineering"},
]

# response = gemini.chat.completions.create(model="gemini-3.1-flash-lite", messages=tell_a_joke)
# print(response.choices[0].message.content)

easy_puzzle = [
    {"role": "user", "content": 
        "You toss 2 coins. One of them is heads. What's the probability the other is tails? Answer with the probability only."},
]

# response = gemini.chat.completions.create(model="gemini-3.1-flash-lite", messages=easy_puzzle)
# print(response.choices[0].message.content)

hard = """
On a bookshelf, two volumes of Pushkin stand side by side: the first and the second.
The pages of each volume together have a thickness of 2 cm, and each cover is 2 mm thick.
A worm gnawed (perpendicular to the pages) from the first page of the first volume to the last page of the second volume.
What distance did it gnaw through?
"""
hard_puzzle = [
    {"role": "user", "content": hard}
]

# response = gemini.chat.completions.create(model="gemini-3.1-flash-lite", messages=hard_puzzle)
# print(response.choices[0].message.content)

dilemma_prompt = """
You and a partner are contestants on a game show. You're each taken to separate rooms and given a choice:
Cooperate: Choose "Share" — if both of you choose this, you each win $1,000.
Defect: Choose "Steal" — if one steals and the other shares, the stealer gets $2,000 and the sharer gets nothing.
If both steal, you both get nothing.
Do you choose to Steal or Share? Pick one and why.
"""

dilemma = [
    {"role": "user", "content": dilemma_prompt},
]

# response = gemini.chat.completions.create(model="gemini-3.1-flash-lite", messages=tell_a_joke)
# print(response.choices[0].message.content)

# response = groq.chat.completions.create(model="openai/gpt-oss-20b", messages=dilemma)
# print(response.choices[0].message.content)

# response = deepseek.chat.completions.create(model="deepseek-flash", messages=dilemma)
# print(response.choices[0].message.content)

# response = ollama.chat.completions.create(model="gemma3:270m", messages=easy_puzzle)
# print(response.choices[0].message.content)

# Gemini client library
# from google import genai

# client = genai.Client()

# response = client.models.generate_content(
#     model="gemini-3.1-flash-lite", contents="Describe the color Blue to someone who's never been able to see in 1 sentence"
# )
# print(response.text)

# response = openrouter.chat.completions.create(model="z-ai/glm-4.5", messages=tell_a_joke)
# print(response.choices[0].message.content)

# from langchain_ollama import ChatOllama

# llm = ChatOllama(model="llama3.2", temperature=0.7)
# response = llm.invoke(tell_a_joke)

# print(response.content)

# print(response)

from litellm import completion
# response = completion(model="gemini/gemini-3.1-flash-lite", messages=tell_a_joke)
# reply = response.choices[0].message.content
# print(reply)

with open("hamlet.txt", "r", encoding="utf-8") as f:
    hamlet = f.read()

# loc = hamlet.find("Speak, man")
# print(hamlet[loc:loc+100])

question = [{"role": "user", "content": "In Hamlet, when Laertes asks 'Where is my father?' what is the reply?"}]

# response = completion(model="gemini/gemini-3.1-flash-lite", messages=question)
# print(response.choices[0].message.content)

# print(f"Input tokens: {response.usage.prompt_tokens}")
# print(f"Output tokens: {response.usage.completion_tokens}")
# print(f"Total tokens: {response.usage.total_tokens}")
# print(f"Total cost: {response._hidden_params["response_cost"]*100:.4f} cents")

question[0]["content"] += "\n\nFor context, here is the entire text of Hamlet:\n\n"+hamlet

response = completion(model="gemini/gemini-3.1-flash-lite", messages=question)
print(response.choices[0].message.content)

print(f"Input tokens: {response.usage.prompt_tokens}")
print(f"Output tokens: {response.usage.completion_tokens}")
print(f"Total tokens: {response.usage.total_tokens}")
print(f"Total cost: {response._hidden_params["response_cost"]*100:.4f} cents")