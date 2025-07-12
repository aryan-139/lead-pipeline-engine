from fastapi import APIRouter
from app.models.schema import TriggerRequest

router = APIRouter()

@router.post("/trigger")
async def trigger_action(req: TriggerRequest):
    if req.intent == "referral":
        print(f"\n🚀 Triggered for Company: {req.company_name}")
        print("📦 Stack Content:")
        for i, item in enumerate(req.lead_list, 1):
            print(f"{i}: {item}")
        return {
            "status": "success",
            "received": len(req.lead_list),
            "company": req.company_name
        }

    return {"status": "error", "message": f"Unknown intent: {req.intent}"}
