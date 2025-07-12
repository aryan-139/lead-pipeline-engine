from fastapi import APIRouter
from app.models.schema import TriggerRequest
from app.core.constants import IntentEnum
from app.services.tokenizer import process_lead

router = APIRouter()

@router.post("/trigger")
async def trigger_action(req: TriggerRequest):
    match req.intent:
        case IntentEnum.REFERRAL:
            all_chunks = []
            
            for i, raw_item in enumerate(req.lead_list, 1):
                chunk = process_lead(raw_item)
                all_chunks.append(chunk)
            
            return {
                "status": "success",
                "received": len(req.lead_list),
                "company": req.company_name,
                "chunks": all_chunks,
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
