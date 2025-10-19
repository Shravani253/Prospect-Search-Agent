import os
import json
import requests

# 🔑 Your People Data Labs API key
PDL_API_KEY = "3ab96f243ab47f1a55b450e4d8a3ca51f500dffd48a263e2684a09fe9f93d3f1"

# -------------------------------------------
# Helper function: fetch data with caching
# -------------------------------------------
def fetch_with_cache(cache_file, url, payload):
    """
    Check if a cached response exists for this request.
    If yes -> load from local cache (saves API credits).
    If no -> call the API once and store response locally.
    """
    if os.path.exists(cache_file):
        print(f"🗂️ Loading cached contacts from {cache_file}")
        with open(cache_file, "r", encoding="utf-8") as f:
            return json.load(f)

    print("🌐 Fetching new contacts from API...")
    try:
        response = requests.post(url, json=payload)
        data = response.json()
    except Exception as e:
        print(f"⚠️ API error: {e}")
        data = {"data": []}

    # Save to cache for reuse
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return data


# -------------------------------------------
# Main function: fetch contacts by domain
# -------------------------------------------
def fetch_contacts_by_domain(domain, size=3):
    """
    Fetch contact info for a company domain using PDL API.
    Automatically caches responses to save API credits.
    """
    if not domain:
        return []

    url = "https://api.peopledatalabs.com/v5/person/search"

    payload = {
        "api_key": PDL_API_KEY,
        "query": {
            "bool": {
                "must": [
                    {"term": {"work_email_domains": domain}}
                ],
                "should": [
                    {"match": {"job_title": "CTO"}},
                    {"match": {"job_title": "VP"}},
                    {"match": {"job_title": "Data"}},
                    {"match": {"job_title": "Engineering"}}
                ],
                "minimum_should_match": 1
            }
        },
        "size": size
    }

    # Cache file per company domain
    safe_domain = domain.replace(".", "_")
    cache_file = f"cache_contacts_{safe_domain}.json"

    # Fetch (cached or fresh)
    data = fetch_with_cache(cache_file, url, payload)
    contacts = []

    # Extract contact details
    for person in data.get("data", []):
        contacts.append({
            "name": person.get("full_name"),
            "title": person.get("job_title"),
            "email": person.get("work_email"),
            "linkedin": person.get("linkedin_url")
        })

    return contacts


# -------------------------------------------
# Manual test (optional)
# -------------------------------------------
if __name__ == "__main__":
    # Try with one company domain (will use 1 credit the first time)
    domain = "openai.com"
    contacts = fetch_contacts_by_domain(domain)
    print(json.dumps(contacts, indent=2))
