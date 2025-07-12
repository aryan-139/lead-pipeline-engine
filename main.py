from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from collections import deque

app = FastAPI()

# In-memory stack to hold text items
text_stack = []

# Allow CORS for all origins (needed for Chrome extension to call this API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # You can restrict this to ["chrome-extension://<EXT_ID>"] for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "FastAPI Text Stack Server is running."}


@app.post("/add")
async def add_text(request: Request):
    data = await request.json()
    text = data.get("value", "")  # expects {"value": "some_text"}
    if text:
        text_stack.append(text)
        print("\n Current Stack:")
        for i, item in enumerate(text_stack, 1):
            print(f"{i}: {item}")
        return {"status": "success", "added_text": text}
    return {"status": "error", "message": "No text provided"}

@app.get("/stack")
def get_stack():
    return text_stack

# write the trigger logic 
@app.post("/trigger")
async def trigger_action(request: Request):
    data = await request.json()
    intent = data.get("intent", "")
    company_name = data.get("company_name", "")
    lead_list_raw = data.get("lead_list", [])
    job_description = data.get("job_description", "")

    if intent == "referral":
        print(f"\n🚀 Triggered for Company: {company_name}")
        print("📦 Stack Content:")
        for i, item in enumerate(lead_list_raw, 1):
            print(f"{i}: {item}")
        return {"status": "success", "received": len(lead_list_raw), "company": company_name}

    return {"status": "error", "message": f"Unknown action: {action}"}
