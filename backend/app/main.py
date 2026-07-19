from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import router as api_router

app = FastAPI(title="VoxBrief AI API", version="1.0.0")
# Allow CORS for the frontend running on localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Router for the API endpoints with a prefix of /api
app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
   # Status endpoint to check if the backend server is running
    return {
        "status": "online",
        "project": "VoxBrief AI Meeting Summarizer",
        "message": "Welcome to the backend local server!"
    }