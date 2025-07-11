from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from collections import deque

app = FastAPI()

# In-memory stack to hold text items
text_stack = []

# Allow CORS for all origins (needed for Chrome extension to call this API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to ["chrome-extension://<EXT_ID>"] for security
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
    text = data.get("value", "") # expects {"value": "some_text"}
    if text:
        text_stack.append(text)
        print("\n Current Stack:")
        for i, item in enumerate(text_stack, 1):
            print(f"{i}: {item}")
        return {"status": "success", "added_text": text}
    return {"status": "error", "message": "No text provided"}
