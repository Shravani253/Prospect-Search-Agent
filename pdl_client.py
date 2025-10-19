import json

def fetch_companies_from_pdl(keyword=None, location=None):
    """
    Loads company data from your local client.json file (Clay export).
    Filters companies by keyword (in Description) or location (Country/Location).
    """

    try:
        with open("client.json", "r", encoding="utf-8") as f:
            all_companies = json.load(f)
    except FileNotFoundError:
        print("⚠️ client.json not found! Make sure it's in your project folder.")
        return []

    filtered = []
    for company in all_companies:
        desc = str(company.get("Description", "")).lower()
        loc = str(company.get("Country", "")).lower()
        loc2 = str(company.get("Location", "")).lower()

        # Match by keyword and/or location
        if keyword and keyword.lower() not in desc:
            continue
        if location and (location.lower() not in loc and location.lower() not in loc2):
            continue

        filtered.append({
            "company_name": company.get("Name"),
            "domain": company.get("Domain"),
            "industry": company.get("Primary Industry"),
            "employee_count": company.get("Employee Count"),
            "description": company.get("Description"),
            "location": company.get("Location"),
            "country": company.get("Country")
        })

    return filtered[:5]  # return top 5 for consistency


if __name__ == "__main__":
    companies = fetch_companies_from_pdl(keyword="AI", location="United States")
    print(json.dumps(companies, indent=2, ensure_ascii=False))
