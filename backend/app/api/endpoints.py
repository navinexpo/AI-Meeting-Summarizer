import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.whisper_service import WhisperService
from app.services.llm_service import LLMService
from app.schemas.meeting import QuestionRequest
# The code defines an API router for handling audio processing and question answering related to meeting transcripts. It uses the WhisperService to transcribe audio files and the LLMService to analyze the transcript and answer questions. The router includes two endpoints: one for processing audio files and another for asking questions about the transcript. It also includes validation for allowed file types and content types, as well as error handling for various scenarios.
router = APIRouter()
whisper_service = WhisperService()
llm_service = LLMService()

ALLOWED_EXTENSIONS = {".mp3", ".wav", ".m4a", ".webm", ".mp4", ".mpeg", ".opus"}
ALLOWED_CONTENT_TYPES = {"audio/", "video/mpeg", "video/mp4"}
# Define a POST endpoint to process audio files and return the transcript and analysis
@router.post("/process")
# Define an asynchronous function to handle the audio processing
async def process_audio(file: UploadFile = File(...)):
    file_ext = os.path.splitext(file.filename)[1].lower()
  
    is_valid_type = any(file.content_type.startswith(t) for t in ALLOWED_CONTENT_TYPES) or file.content_type in ALLOWED_CONTENT_TYPES
    # fixing the issue with the file extension check to ensure it is case-insensitive
    if file_ext not in ALLOWED_EXTENSIONS and not is_valid_type:
        raise HTTPException(status_code=400, detail="Invalid audio or video format")
  
    temp_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data/storage"))
    os.makedirs(temp_dir, exist_ok=True)
    
    temp_file_path = os.path.join(temp_dir, file.filename)
   
    try:
        with open(temp_file_path, "wb") as f:
            content = await file.read()
            f.write(content)
            
        transcript = whisper_service.transcribe_audio(temp_file_path)
        analysis = llm_service.analyze_transcript(transcript)
    
        return {
            "status": "success",
            "transcript": transcript,
            "analysis": analysis
        }
    
        raise HTTPException(status_code=500, detail=str(e))
        
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
#  Route to handle question answering about the transcript
@router.post("/ask-question")
async def ask_question_about_transcript(payload: QuestionRequest):
    try:
        if not payload.transcript.strip() or not payload.question.strip():
            raise HTTPException(status_code=400, detail="Transcript and question cannot be empty")
            
        answer = llm_service.ask_question(payload.transcript, payload.question)
        return {
            "status": "success",
            "answer": answer
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))