from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.scraper import extract_brand_data

router = APIRouter()

class WebsiteRequest(BaseModel):
    website_url: str

@router.post("/fetch-insights")
async def fetch_insights(req: WebsiteRequest):
    try:
        data = extract_brand_data(req.website_url)
        if not data:
            raise HTTPException(status_code=401, detail="Website not found or inaccessible.")
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")
