import os
import httpx
from groq import Groq
from app.core.config import settings
# Update origin in httpx.Client() to match your server's origin if needed
class WhisperService:
    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY, http_client=httpx.Client())
    # Transcribe audio file using the Whisper model
    def transcribe_audio(self, file_path: str) -> str:
        if not os.path.exists(file_path):
            raise FileNotFoundError("Audio file not found on server")
      # Audio transcription is performed using the Whisper model, which is designed to handle various audio inputs, including music and speech. The prompt instructs the model to focus on transcribing lyrics if music is detected in the audio file. The response format is set to "text" to receive a plain text transcription of the audio content.
        with open(file_path, "rb") as audio_file:
            translation = self.client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-large-v3",
                response_format="text",
                prompt="Transcribe the lyrics of the song carefully if music is playing.",
                # Translation parameters
                language="en",
                temperature=0.0
            )
          # The translation variable contains the transcribed text from the audio file, which is returned as a string. This allows for further processing or analysis of the transcribed content in other parts of the application.
        return translation