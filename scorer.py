def score_company(company, icp):
    score = 0.4  # base

    # industry match
    if company.get("industry") in icp.get("industry", []):
        score += 0.2

    # employee size match
    if company.get("employee_count") and company["employee_count"] >= icp["employee_count_min"]:
        score += 0.2

    # at least 1 contact
    if company.get("contacts"):
        score += 0.2

    return round(score, 2)
