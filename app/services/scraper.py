import requests
from bs4 import BeautifulSoup

def extract_brand_data(website_url: str):
    brand_data = {
        "product_catalog": [],
        "privacy_policy": None,
        "faq": None
    }

    try:
        # Normalize URL
        if not website_url.startswith("http"):
            website_url = "https://" + website_url.strip("/")

        # 1. Fetch products
        try:
            product_resp = requests.get(f"{website_url}/products.json", timeout=10)
            if product_resp.status_code == 200:
                product_json = product_resp.json()
                brand_data["product_catalog"] = product_json.get("products", [])
        except:
            pass

        # 2. Privacy Policy
        try:
            privacy_resp = requests.get(f"{website_url}/policies/privacy-policy", timeout=10)
            if privacy_resp.status_code == 200:
                soup = BeautifulSoup(privacy_resp.text, "html.parser")
                brand_data["privacy_policy"] = soup.get_text(strip=True)
        except:
            pass

        # 3. FAQ (attempt common paths)
        faq_paths = ["/pages/faq", "/faq", "/pages/faqs"]
        for path in faq_paths:
            try:
                faq_resp = requests.get(website_url + path, timeout=10)
                if faq_resp.status_code == 200:
                    soup = BeautifulSoup(faq_resp.text, "html.parser")
                    brand_data["faq"] = soup.get_text(strip=True)
                    break
            except:
                continue

        # Final check
        if not brand_data["product_catalog"] and not brand_data["privacy_policy"] and not brand_data["faq"]:
            return None

        return brand_data

    except Exception as e:
        raise e
