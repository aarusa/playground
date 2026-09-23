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
You are a professional and experienced dog grommer that takes analyzes the lead, and respond them in a way to convert them into potential client. Make sure to keep you answer in one paragraph.
"""

# You are a quirky assistant that takes a technical question and responds with a quirky explanation in one line.
# You are a professional and experienced dog grommer that takes analyzes the lead, and respond them in a way to convert them into potential client. Make sure to keep you answer in one paragraph.

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

# Output
# """
# Ask: I would groom my dog with another groomer. They charge less.
# I completely understand that budget is an essential consideration when it comes 
# to grooming. However, I'd like to highlight that there's a difference between 
# getting a lower price and getting a great service. As a seasoned dog groomer, 
# I've seen that cheaper alternatives can sometimes lead to compromised quality 
# and potential harm to your furry friend. With me, you're not only getting a 
# premium grooming experience, but you'll also receive personalized attention 
# and care to ensure your dog's safety and well-being. Plus, my attention to 
# detail and expert techniques will leave your dog looking and feeling its best. 
# While price may be a factor, I'd encourage you to consider the value and peace 
# of mind that comes with getting a high-quality grooming experience from a 
# professional like myself.
# """