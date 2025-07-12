from pydantic import BaseModel
from typing import List
from enum import Enum

class IntentEnum(str, Enum):
    referral = "referral"
    opening_enquiry = "opening_enquiry"

class AddTextRequest(BaseModel):
    value: str

class TriggerRequest(BaseModel):
    intent: IntentEnum
    company_name: str
    job_description: str
    lead_list: List[str]
