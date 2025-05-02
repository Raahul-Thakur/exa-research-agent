import os
from exa_py import Exa

from tools.limits import check_limit

def search_exa(query: str, num_results: int = 5) -> str:
    if not check_limit():
        return "❌ Monthly usage limit reached (1,000 requests). Please try again later."

def search_exa(query: str, num_results: int = 5) -> str:
    try:
        # Load API key
        api_key = os.getenv("EXA_API_KEY")
        print("[DEBUG] EXA_API_KEY =", api_key)

        if not api_key:
            return "❌ EXA_API_KEY is not set."

        # Initialize Exa client
        exa = Exa(api_key=api_key)

        print(f"[DEBUG] Querying Exa: {query}")
        results = exa.search(query, num_results=num_results)

        print("[DEBUG] Raw Exa response:", results)

        # Check if response is valid
        if results is None:
            return "❌ Exa API returned None. Check your API key or query."

        if not hasattr(results, "results") or not results.results:
            return "❌ No results found."

        # Format output
        output = ""
        for idx, r in enumerate(results.results, 1):
            title = r.title or "Untitled"
            url = r.url or "No URL"
            snippet = r.text or r.summary or "No preview text available."

            output += f"🔹 **{idx}. {title}**\n"
            output += f"🔗 {url}\n"
            output += f"📝 {snippet[:300]}...\n\n"

        return output

    except Exception as e:
        print(f"[ERROR] Exception during Exa search: {e}")
        return f"❌ EXA API Error: {str(e)}"
