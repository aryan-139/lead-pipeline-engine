from pydantic import BaseModel
from typing import List
from enum import Enum


class IntentEnum(str, Enum):
    referral = "referral"
    opening_enquiry = "opening_enquiry"


from enum import Enum


class EmailFormatEnum(str, Enum):
    # Top 3 most widely used patterns (90%+ use cases)
    first_last = "first_last"  # aryanraj
    first_period_last = "first_period_last"  # aryan.raj
    first_initial_last = "first_initial_last"  # araj
    first_initial_period_last = "first_initial_period_last"  # a.raj

    first_last_initial = "first_last_initial"  # aryanr
    first_period_last_initial = "first_period_last_initial"  # aryan.r

    first_initial_last_initial = "first_initial_last_initial"  # a.r / ar
    last_first = "last_first"  # rajaryan
    last_first_initial = "last_first_initial"  # raja


class AddTextRequest(BaseModel):
    value: str


class TriggerRequest(BaseModel):
    intent: IntentEnum
    company_name: str
    job_description: str
    lead_list: List[str]
    custom_address: str = None
    email_format: EmailFormatEnum = EmailFormatEnum.first_last
