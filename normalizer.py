def normalize_pdl_company(raw):
    """
    Takes one company dictionary from client.json and standardizes it.
    """
    return {
        "company_name": raw.get("company_name") or raw.get("Name"),
        "domain": raw.get("domain") or raw.get("Domain"),
        "industry": raw.get("industry") or raw.get("Primary Industry"),
        "employee_count": raw.get("employee_count") or raw.get("Employee Count"),
        "location": raw.get("location") or raw.get("Location"),
        "country": raw.get("country") or raw.get("Country"),
        "description": raw.get("description") or raw.get("Description"),
        "contacts": [],  # to be filled from pdl_contacts
        "signals": {},   # to be filled from signals.py
        "source": ["Local JSON"],
        "confidence": 0.0
    }
