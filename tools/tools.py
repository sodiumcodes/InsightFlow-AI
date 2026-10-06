from dotenv import load_dotenv
load_dotenv()

import os
import requests
from langchain.tools import tool
from bs4 import BeautifulSoup
from tavily import TavilyClient
from rich import print
tavily = TavilyClient(api_key= os.getenv("TAVILY_API_KEY"))

@tool
def do_web_search(query:str) ->str:
    """Searches the web for recent and reliable information on a topic. Returns titles, url, snippets"""
    results = tavily.search(query=query, max_results=3)
    out = []

    for r in results['results']:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
        )

    return "\n".join(out)

@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        # BeautifulSoup parses that HTML so you can work with its elements.
        soup = BeautifulSoup(resp.text, "html.parser")

        for tag in soup(["script", "style", "nav", "footer"]):
            # Completely removes that HTML element from the parsed webpage.
            tag.decompose()

        return soup.get_text(separator=" ", strip=True)[:3000]
    
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"



