SHOPIFY BRAND CONTEXT SCRAPER

This project is a FastAPI application that scrapes key brand information from a given Shopify store URL and returns a structured JSON response. It pulls product catalog, policies, FAQs, and "About Us" content from the store.

-----------------------------------------
FEATURES
-----------------------------------------
- Scrapes data from Shopify stores using public endpoints.
- Returns product list, privacy/refund policies, FAQs, About Us content.
- Handles errors for invalid or non-Shopify sites.
- FastAPI backend with async support using httpx and BeautifulSoup.

-----------------------------------------
HOW TO RUN LOCALLY
-----------------------------------------
1. Clone the GitHub repository
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME

2. Navigate into the project folder
   cd YOUR_REPO_NAME

3. Create a virtual environment (optional but recommended)
   python -m venv venv
   venv\Scripts\activate     (on Windows)
   source venv/bin/activate  (on Mac/Linux)

4. Install dependencies
   pip install -r requirements.txt

5. Start the FastAPI server
   uvicorn app.main:app --reload

6. Visit the API Docs in your browser:
   http://localhost:8000/docs

-----------------------------------------
EXAMPLE USAGE
-----------------------------------------
POST /fetch-insights
Request Body (JSON):
{
  "website_url": "https://memy.co.in"
}

Response:
{
  "brand_name": "MeMy",
  "product_catalog": [...],
  "policies": {
    "privacy_policy": "...",
    "refund_policy": "..."
  },
  "faqs": [...],
  "about_us": "..."
}

-----------------------------------------
TECH STACK
-----------------------------------------
- Python
- FastAPI
- httpx
- BeautifulSoup
- Pydantic

-----------------------------------------
LICENSE
-----------------------------------------
MIT License - Free to use and modify.
