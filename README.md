# Ryzosphere AI Scraper PoC

A proof-of-concept pipeline that scrapes publicly available agricultural market information and converts it into structured JSON using a large language model.

## Why I Built This

I wanted to explore a different approach to web scraping. Instead of relying on complex HTML parsing rules that can easily break when a website changes, this project uses an LLM to interpret scraped content and organize it into a consistent schema.

The project simulates a small data pipeline by collecting information from an agricultural market, validating the output, and saving the structured data locally.

## What It Does

- Scrapes agricultural market pages using `requests` and `BeautifulSoup`
- Uses a custom User-Agent and rate limiting to avoid overwhelming websites
- Sends the scraped content to Google's Gemini model for structured extraction
- Validates the response against a predefined JSON schema
- Stores validated results in a local staging folder

## Example Output

When the scraper is run, it fetches market information, sends the scraped text to Gemini for structured extraction, validates the result, and saves the output locally.

**Console Output**

```text
Fetching data from https://en.wikipedia.org/wiki/Union_Square_Greenmarket...
Respecting rate limits: Sleeping for 2 seconds before request...
Successfully fetched the page!

Handing raw text over to the AI Agent for structuring...

=== THE FINAL STRUCTURED DATA ===
{
  "market_name": "Union Square",
  "location": "Union Square Park, Manhattan, New York City"
}

Success! Validated data written to staging_output/market_data_v1.json
```

**Generated JSON**

```json
{
  "market_name": "Union Square",
  "location": "Union Square Park, Manhattan, New York City"
}
```

## Project Structure

```
.
├── scraper.py          # Main pipeline
├── schema.json         # Expected JSON format
├── .env                # Gemini API key
├── .gitignore          # Allows encrypted info to stay hidden after pushing code to GitHub
└── README.md
```

## Technologies

- Python
- Requests
- BeautifulSoup
- Google Gemini API
- JSON
- python-dotenv

## Running the Project

1. Clone the repository

```bash
git clone https://github.com/Tife-O/Ryzosphere-AI-Scraper-PoC.git
cd Ryzosphere-AI-Scraper-PoC
```

2. Create a virtual environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

macOS/Linux

```bash
source venv/bin/activate
```

3. Install dependencies

```bash
pip install requests beautifulsoup4 google-genai python-dotenv
```

4. Create a `.env` file

```text
GEMINI_API_KEY=your_api_key_here
```

5. Run the scraper

```bash
python scraper.py
```

## Future Improvements

- Support scraping multiple markets
- Add retry logic for failed requests
- Export results to a database
- Add automated tests