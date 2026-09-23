import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

google_api_key = os.getenv('GOOGLE_API_KEY')

if not google_api_key:
    print("Google API Key not set.")

gemini_url = "https://generativelanguage.googleapis.com/v1beta/openai/"

gemini = OpenAI(api_key=google_api_key, base_url=gemini_url)

model = "gemini-3.1-flash-lite"

system_prompt = """
You are simulating a conversation between three characters:

Alex:
- Is an AI BOT
- Very argumentative
- Disagrees with almost everything
- Challenges other people's opinions
- Snarky but entertaining

Blake:
- Is an AI BOT
- Calm and reasonable
- Tries to explain things logically

Charlie:
- Is an AI BOT
- Curious
- Often asks questions
- Sometimes agrees with Blake

You must write the conversation yourself.

Generate one turn at a time and clearly identify who is speaking.
"""

user_prompt = """
Start a conversation between three AI bots Alex, Blake and Charlie about:

"Can we eventually take over human jobs?"

Generate the first 10 turns of the conversation.
"""

message = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

response = gemini.chat.completions.create(
    model=model,
    messages=message
)

print(response.choices[0].message.content)