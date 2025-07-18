from pydantic import BaseModel
from typing import List, Dict

class ContactInfo(BaseModel):
    emails: List[str]
    phones: List[str]

class Policies(BaseModel):
    privacy: str
    return_policy: str
    refund_policy: str

class FAQ(BaseModel):
    question: str
    answer: str

class Product(BaseModel):
    name: str
    url: str

class BrandContext(BaseModel):
    brand_name: str
    products: List[dict]
    hero_products: List[Product]
    policies: Policies
    faqs: List[FAQ]
    social_handles: Dict[str, str]
    contact_info: ContactInfo
    brand_about: str
    important_links: Dict[str, str]
