from fastapi import APIRouter
from app.models.schema import TriggerRequest
from app.core.constants import IntentEnum
from app.services.tokenizer import process_lead
from app.services.emailer import create_email

router = APIRouter()

@router.post("/trigger")
async def trigger_action(req: TriggerRequest):
    match req.intent:
        case IntentEnum.REFERRAL:
            all_valid_emails = []
            
            for i, raw_item in enumerate(req.lead_list, 1):
                chunk = process_lead(raw_item)
                # create email
                email= create_email(chunk, req.company_name, req.custom_address, req.email_format)
                all_valid_emails.append(email)
                print(f"\n{i}. {raw_item} -> {email}")
            
            
            return {
                "status": "success",
                "intent": req.intent,
                "received": len(req.lead_list),
                "company": req.company_name,
                "emails": all_valid_emails,
            }

        case IntentEnum.OPENING_ENQUIRY:
            # Placeholder for opening enquiry logic
            # print(f"\n🔍 Opening Enquiry for: {req.company_name}")
            return {
                "status": "success",
                "message": "Opening enquiry logic handled",
                "company": req.company_name
            }

    #     case _:
    #         return {
    #             "status": "error",
    #             "message": f"Unknown intent: {req.intent}"
    #         }
