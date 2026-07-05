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
        # model="whisper-large-v3" is used for better accuracy in transcription
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
            # The response from the Whisper model is expected to be a text string containing the transcribed content of the audio file. The prompt instructs the model to focus on accurately transcribing lyrics if music is present, ensuring that the output is clear and suitable for further processing or display in the application.
        return translation