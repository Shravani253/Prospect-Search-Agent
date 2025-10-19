def fake_signal_generator(company_name):
    company_name = company_name or ""
    return {
        "recent_funding": "AI" in company_name.upper(),
        "recent_hiring": "DATA" in company_name.upper()
    }
