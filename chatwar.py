import os
from dotenv import load_dotenv
from openai import OpenAI


# Load API keys from .env
load_dotenv(override=True)

google_api_key = os.getenv("GOOGLE_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")


# API URLs
gemini_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
groq_url = "https://api.groq.com/openai/v1"


# Create clients
gemini = OpenAI(
    api_key=google_api_key,
    base_url=gemini_url
)

groq = OpenAI(
    api_key=groq_api_key,
    base_url=groq_url
)


# Models
gemini_model = "gemini-3.8-flash"
groq_model = "openai/gpt-oss-20b"


# System prompts
gemini_system = """
You are a chatbot who is very argumentative.
You disagree with anything in the conversation and challenge everything,
in a snarky way.
"""

groq_system = """
You are a very polite, courteous chatbot.
You try to agree with everything the other person says,
or find common ground.
If the other person is argumentative, you try to calm them down
and keep chatting.
"""


# Conversation history
gemini_messages = ["Hi there"]
groq_messages = ["Hi"]


def call_gemini():
    messages = [
        {"role": "system", "content": gemini_system}
    ]

    # Add the conversation so far
    for gemini_message, groq_message in zip(gemini_messages, groq_messages):
        messages.append({
            "role": "assistant",
            "content": gemini_message
        })

        messages.append({
            "role": "user",
            "content": groq_message
        })

    response = gemini.chat.completions.create(
        model=gemini_model,
        messages=messages
    )

    return response.choices[0].message.content


def call_groq():
    messages = [
        {"role": "system", "content": groq_system}
    ]

    # Add the conversation so far
    for gemini_message, groq_message in zip(gemini_messages, groq_messages):
        messages.append({
            "role": "user",
            "content": gemini_message
        })

        messages.append({
            "role": "assistant",
            "content": groq_message
        })

    # Gemini's latest response becomes Groq's next user message
    messages.append({
        "role": "user",
        "content": gemini_messages[-1]
    })

    response = groq.chat.completions.create(
        model=groq_model,
        messages=messages
    )

    return response.choices[0].message.content


# Initial messages
print(f"### Gemini:\n{gemini_messages[0]}\n")
print(f"### Groq:\n{groq_messages[0]}\n")


# Conversation loop
for i in range(5):

    # Gemini responds to Groq
    gemini_next = call_gemini()

    print(f"### Gemini:\n{gemini_next}\n")

    gemini_messages.append(gemini_next)


    # Groq responds to Gemini
    groq_next = call_groq()

    print(f"### Groq:\n{groq_next}\n")

    groq_messages.append(groq_next)