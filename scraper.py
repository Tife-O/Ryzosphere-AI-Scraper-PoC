import os
import requests
from bs4 import BeautifulSoup
import time
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()
TARGET_URL = "https://en.wikipedia.org/wiki/Union_Square_Greenmarket"



def fetch_market_data(url):
    print(f"Fetching data from {url}...")
    print("Respecting rate limits: Sleeping for 2 seconds before request...")
    time.sleep(2)

    headers = {
        "User-Agent": "Ryzosphere-PoC-Bot/1.0 (Student Project; tifeodepe@gmail.com)"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Successfully fetched the page!")
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find(id="mw-content-text")
        raw_text = content.get_text(separator=' ', strip=True) 
        return raw_text[:3000]
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def run_ai_agent(raw_text):
    print("\nHanding raw text over to the AI Agent for structuring...")
    with open("schema.json", "r") as f:
        schema_data = json.load(f)

    prompt = f"""
    You are a data pipeline agent for The Ryzosphere. 
    Extract the farmers market details from the following raw text. 
    You must strictly follow the schema provided in the configuration.
    
    Raw Text:
    {raw_text}
    """
    response = client.models.generate_content(
        model='gemini-3.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=schema_data,
        ),
    )
    return response.text

if __name__ == "__main__":
    text_data = fetch_market_data(TARGET_URL)
    
    if text_data:
        structured_json = run_ai_agent(text_data)
        
        print("\n=== THE FINAL STRUCTURED DATA ===")
        print(structured_json)
        staging_dir = "staging_output"
        os.makedirs(staging_dir, exist_ok=True)
        
        file_path = os.path.join(staging_dir, "market_data_v1.json")
        
        with open(file_path, "w") as f:
            f.write(structured_json)
            
        print(f"\nSuccess! Validated data written to staging location: {file_path}")