import os
from dotenv import load_dotenv
from openai import OpenAI
from scraper import fetch_website_contents

# Load environment variables
load_dotenv(override=True)
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")

if not OLLAMA_BASE_URL:
    raise ValueError("OLLAMA_BASE_URL is not set in the .env file or environment variables.")

# Initialize OpenAI client pointing to Ollama
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')

# Define our system prompt - you can experiment with this later, changing the last sentence to 'Respond in markdown in Spanish."
system_prompt = """
You are a snarky assistant that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""

# Define our user prompt
user_prompt_prefix = """
Here are the contents of a portfolio website.
Provide a short summary of this website.
If it includes projects or blogs, then summarize these too.
Also tell me if I should hire this candidate for my company.
Rate her out of 10 and what are areas of improvement.
"""

DEFAULT_MODEL = "llama3.2"

# Construct the chat message payload for the LLM
def messages_for(website_content):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website_content}
    ]

# Fetches wesite content and generates a summary using Ollama
def summarize(url):
    website_content = fetch_website_contents(url)
    response = ollama.chat.completions.create(
        model = DEFAULT_MODEL,
        messages = messages_for(website_content)
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    target_url = "https://arusha.com.np"
    summary_result = summarize(target_url)
    print("\n--- Summary Result ---\n")
    print(summary_result)
