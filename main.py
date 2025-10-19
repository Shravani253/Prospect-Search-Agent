from fastapi import FastAPI
import json
from pdl_client import fetch_companies_from_pdl
from pdl_contacts import fetch_contacts_by_domain
from normalizer import normalize_pdl_company
from scorer import score_company
from signals import fake_signal_generator

app = FastAPI()

# Root route (just to check if server is running)
@app.get("/")
def home():
    return {"message": "Server is running"}

# Main endpoint to run the agent
@app.post("/run_agent")
def run_agent():
    try:
        # Load ICP config
        with open("icp_config.json", "r", encoding="utf-8") as f:
            ICP = json.load(f)
    except FileNotFoundError:
        return {"error": "icp_config.json file not found!"}

    keywords = ICP.get("keywords", [])
    results = []

    for kw in keywords:
        print(f"🔎 Fetching companies for keyword: {kw}")
        companies = fetch_companies_from_pdl(keyword=kw, location="United States")
        print(f"Found {len(companies)} companies for '{kw}'")

        for c in companies:
            normalized = normalize_pdl_company(c)

            # Fetch contacts
            contacts = fetch_contacts_by_domain(normalized["domain"])
            normalized["contacts"] = contacts

            # Add dummy signals
            normalized["signals"] = fake_signal_generator(normalized["company_name"])

            # Score
            normalized["confidence"] = score_company(normalized, ICP)

            results.append(normalized)

    # Save results
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"✅ Done! Saved {len(results)} companies to output.json")
    return {"status": "Done", "companies_fetched": len(results)}
