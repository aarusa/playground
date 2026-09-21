import os
import json
from dotenv import load_dotenv
from scraper import fetch_website_links, fetch_website_contents
from openai import OpenAI

load_dotenv(override=True)
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")

if not OLLAMA_BASE_URL:
    raise ValueError("OLLAMA_BASE_URL is not set in the .env file or environment variables.")

# Initialize OpenAI client pointing to Ollama
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')

DEFAULT_MODEL = "llama3.2"

website = "https://edwarddonner.com"

links = fetch_website_links(website)

link_system_prompt = """
You are provided with a list of links found on a webpage.
You are able to decide which of the links would be most relevant to include in a brochure about the company, such as links to an About page, or a Company page, or Careers/Jobs pages.
You should respond in JSON as in the example:
{
    "links": [
        {"type": "about page", "url": "https://full.url/goes/here/about"},
        {"type": "careers page", "url": "https://another.full.url/careers"}
    ]
}
"""

def get_links_user_prompt(url):
    user_prompt = f"""
Here is the list of links on the website {url} -
Please decide which of these are relevant web links for a brochure about the company, 
respond with the full https URL in JSON format.
Do not include Terms of Service, Privacy, email links.

Links (some might be relative links):

"""
    links = fetch_website_links(url)
    user_prompt += "\n".join(links)
    return user_prompt

# print(get_links_user_prompt(website))

# def select_relevant_links(url):
#     response = ollama.chat.completions.create(
#         model=DEFAULT_MODEL,
#         messages=[
#             {"role": "system", "content": link_system_prompt},
#             {"role": "user", "content": get_links_user_prompt(url)}
#         ],
#         response_format={"type": "json_object"}
#     )
#     result = response.choices[0].message.content
#     links = json.loads(result)
#     return links

# print(select_relevant_links(website))

def select_relevant_links(url):
    print(f"Selecting relevant links for {url} by calling {DEFAULT_MODEL}")
    response = ollama.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=[
            {"role": "system", "content": link_system_prompt},
            {"role": "user", "content": get_links_user_prompt(url)}
        ],
        response_format={"type": "json_object"}
    )
    result = response.choices[0].message.content
    links = json.loads(result)
    print(f"Found {len(links['links'])} relevant links")
    return links

print(select_relevant_links(website))


