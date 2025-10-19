# Prospect-Search-Agent
AI-powered B2B Prospect Finder | FastAPI | Data Enrichment | Automated ICP Matching
ProspectSearchAgent
AI-powered B2B Prospect Finder
________________________________________
Overview
ProspectSearchAgent is a Python-based automation tool that discovers and enriches B2B company data based on a given Ideal Customer Profile (ICP).
It identifies companies that match your ICP, adds contact and signal data, and outputs structured insights in JSON format.
________________________________________
Features
•	Fetches and filters company data (API or local file)
•	Matches Ideal Customer Profile (ICP)
•	Normalizes and enriches company data
•	Adds contacts (CTO, VP, Data roles)
•	Adds funding and hiring signals
•	Assigns confidence score
•	Uses FastAPI with Swagger UI
•	Implements caching to save API credits
•	Exports results into output.json
________________________________________
Tech Stack
Python 3.10+
FastAPI
People Data Labs / Clay API
Requests, JSON, OS libraries
Git & GitHub
________________________________________
Project Structure
main.py — main script to run everything
pdl_client.py — fetches company data
pdl_contacts.py — fetches company contacts
normalizer.py — normalizes company info
scorer.py — assigns confidence scores
signals.py — adds funding and hiring signals
icp_config.json — defines ICP parameters
client.json — contains local dataset
output.json — final results
README.md — documentation
________________________________________
Setup Instructions
1.	Clone repository
git clone https://github.com/Shravani253/ProspectSearchAgent.git
cd ProspectSearchAgent
2.	Install dependencies
pip install fastapi uvicorn requests
3.	Add your PDL API key
In pdl_contacts.py and pdl_client.py:
PDL_API_KEY = "3ab96f243ab47f1a55b450e4d8a3ca51f500dffd48a263e2684a09fe9f93d3f1"
4.	Run the project
python main.py
5.	Check output
Open output.json to see the structured company data
________________________________________
Run on FastAPI 
Start server:
uvicorn main:app --reload
Open:
http://127.0.0.1:8000/docs
Use:
GET / → to check server
POST /run_agent → to run the agent
________________________________________
Example Output
{
"company_name": "OpenAI",
"domain": "openai.com",
"industry": "Research Services",
"employee_count": 8626,
"location": "San Francisco, CA",
"country": "United States",
"contacts": [
{"name": "Sarah Green", "title": "VP Engineering", "email": "sarah@openai.com"}
],
"signals": {"recent_funding": true, "recent_hiring": false},
"confidence": 0.8
}
________________________________________
Example ICP Config (Important)
{
"revenue_min": 20000000,
"revenue_max": 200000000,
"industry": ["Software", "FinTech"],
"geography": ["USA"],
"employee_count_min": 100,
"keywords": ["AI", "data analytics", "automation", "machine learning"]
}
________________________________________
Author
Shravani Vanalkar


