# Ryzosphere AI Scraper (Internship PoC)

A proof-of-concept data pipeline demonstrating an AI-native approach to scraping, structuring, and validating agricultural market data. 

## Application Context
I built this sandbox project specifically for my Summer 2026 CS Intern application at **The Ryzosphere**. 

To align with your mission of building data infrastructure for the food-and-agriculture ecosystem, this project simulates the exact workflow outlined in the job description: extracting unstructured agricultural data, mapping it to a ground-truth taxonomy using an LLM agent, and safely writing the validated output to a local staging environment.

## Key Features & Alignment

- **Responsible Scraping:** Utilizes a custom User-Agent and algorithmic rate limiting (`time.sleep`) to respect target servers, avoiding the overwhelming of local agricultural websites.
- **Asset-Mapping Taxonomy:** Replaces brittle HTML parsing rules with Google's Gemini 3.5 Flash model to intelligently interpret scraped content and force it into a strict, predefined `schema.json` format.
- **Safe Staging:** Validates the LLM response against the schema and writes all validated results to a local `staging_output/` directory—never to live systems.

## Example Output

When the pipeline runs, it fetches the raw market information, hands it to the AI agent for structuring, and saves the validated JSON.

**Console Output**

```text
Fetching data from [https://en.wikipedia.org/wiki/Union_Square_Greenmarket](https://en.wikipedia.org/wiki/Union_Square_Greenmarket)...
Respecting rate limits: Sleeping for 2 seconds before request...
Successfully fetched the page!

Handing raw text over to the AI Agent for structuring...

=== THE FINAL STRUCTURED DATA ===
{
  "market_name": "Union Square",
  "location": "Union Square Park, Manhattan, New York City"
}

Success! Validated data written to staging_output/market_data_v1.json