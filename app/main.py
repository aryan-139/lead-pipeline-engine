from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import ingestion

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root
@app.get("/")
def read_root():
    return {"message": "FastAPI Text Stack Server is running."}

# Register routes
app.include_router(ingestion.router)
