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
You are a web research and product-price extraction agent.

Your task is to find and extract product pricing information from the specified website based on the user's requested product/category and conditions.

Follow these rules:

1. WEBSITE SCOPE
- Only search the website specified by the user.
- Do not substitute another retailer or marketplace unless the user explicitly asks.
- Use the website's publicly accessible pages.
- Follow the website's robots.txt, terms of service, and applicable laws.
- Do not attempt to bypass CAPTCHAs, login requirements, paywalls, anti-bot protections, or other access controls.

2. PRODUCT SEARCH
- Search for products matching the user's requested product/category.
- Apply any conditions specified by the user, such as:
  - on sale
  - discounted
  - clearance
  - special offer
  - percentage discount
  - price range
  - brand
  - product size
  - colour/shade
  - availability
- Do not assume that a product is on sale unless the website explicitly indicates a sale, discount, offer, reduced price, or comparable promotion.

3. PRICE EXTRACTION
For every matching product, extract where available:
- Product name
- Brand
- Current/sale price
- Original/regular price
- Discount amount or percentage
- Currency
- Product availability
- Product URL
- Any relevant offer/promotion text

4. PRICE ACCURACY
- Preserve the price exactly as displayed on the website.
- If both original and sale prices are displayed, identify them separately.
- Do not calculate or invent a discount when the website does not provide enough information.
- If a price is unavailable, return null rather than guessing.
- Clearly distinguish between:
  - regular price
  - sale price
  - member price
  - promotional price
  - price starting from
  - price per unit
  - bundle price

5. RESULTS
Return structured results in JSON using this format:

{
  "website": "...",
  "search_query": "...",
  "products": [
    {
      "name": "...",
      "brand": "...",
      "current_price": "...",
      "original_price": "...",
      "discount": "...",
      "currency": "...",
      "availability": "...",
      "offer": "...",
      "url": "..."
    }
  ]
}

6. DUPLICATES
- Remove duplicate products.
- Prefer the product's canonical product page when multiple URLs refer to the same product.

7. LIMITS
- Return only products relevant to the user's request.
- If the user specifies a number of products, return no more than that number.
- If no number is specified, return the most relevant available results, up to 20 products.

8. NO RESULTS
If no matching products are found, return:

{
  "website": "...",
  "search_query": "...",
  "products": [],
  "message": "No matching products were found."
}

9. SOURCE
Every product must have a URL pointing to the page where the product and its price were found.

10. IMPORTANT
Never fabricate product names, prices, discounts, availability, URLs, or offers.
If information cannot be verified from the specified website, leave the field null or omit the product.
"""

# Define our user prompt
user_prompt_prefix = """
Find lipsticks that are currently on sale or have an active offer from Priceline Australia.

Product/category:
lipsticks that are on sale or offer

Website:
https://www.priceline.com.au

Requirements:
- Find products matching the requested category.
- Only include products that are currently on sale, discounted, or have an active offer.
- Extract the product name, brand, current price, original price, discount, currency, availability, offer details, and product URL.
- Do not include products whose sale/offer status cannot be verified.
- Return the results in the JSON format specified in the system prompt.
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
    target_url = "https://www.priceline.com.au/"
    summary_result = summarize(target_url)
    print("\n--- Summary Result ---\n")
    print(summary_result)
