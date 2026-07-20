from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import router as api_router
# Initialize the FastAPI app with a title and version
app = FastAPI(title="VoxBrief AI API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Router for the API endpoints with a prefix of /api
app.include_router(api_router, prefix="/api")
# Application startup event to print a message when the server starts
@app.get("/")
def read_root():
   # Status endpoint to check if the backend server is running
    return {
        "status": "online",
        "project": "VoxBrief AI Meeting Summarizer",
        "message": "Welcome to the backend local server!"
    }