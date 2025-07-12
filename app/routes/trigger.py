from fastapi import APIRouter
from app.models.schema import TriggerRequest
from app.constants import IntentEnum

router = APIRouter()

@router.post("/trigger")
async def trigger_action(req: TriggerRequest):
    match req.intent:
        case IntentEnum.REFERRAL:
            print(f"\n🚀 Triggered for Company: {req.company_name}")
            print("📦 Stack Content:")
            for i, item in enumerate(req.lead_list, 1):
                print(f"{i}: {item}")
            return {
                "status": "success",
                "received": len(req.lead_list),
                "company": req.company_name
            }

        case IntentEnum.OPENING_ENQUIRY:
            # Placeholder for opening enquiry logic
            # print(f"\n🔍 Opening Enquiry for: {req.company_name}")
            return {
                "status": "success",
                "message": "Opening enquiry logic handled",
                "company": req.company_name
            }

        case _:
            return {
                "status": "error",
                "message": f"Unknown intent: {req.intent}"
            }
