import json
import httpx
from groq import Groq
from app.core.config import settings

class LLMService:
    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY, http_client=httpx.Client())
  # Prompt for analyzing the transcript and returning a structured JSON response. The prompt instructs the LLM to provide a summary, key takeaways, and action items based on the provided transcript text.
    def analyze_transcript(self, transcript_text: str) -> dict:
        prompt = (
            "You are an expert meeting assistant. Analyze the following meeting transcript. "
            "You must return the response strictly as a valid JSON object matching this schema:\n"
            "{  \n"
            "  \"summary\": \"A short high-level overview of the meeting\",\n"
            "  \"key_takeaways\": [\"point 1\", \"point 2\"],\n"   
            "  \"action_items\": [\n"
            "    {\"task\": \"task description\", \"owner\": \"person name or Unassigned\", \"deadline\": \"date/time or TBD\"}\n"
            "  ]\n"
            "}\n"
            "Do not include any prose, markdown block, introduction, or conversation before or after the JSON. "
            f"Transcript:\n{transcript_text}"
        )
     
        response = self.client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant",
            response_format={"type": "json_object"},
            temperature=0.2
        )
      
        raw_content = response.choices[0].message.content
        return json.loads(raw_content)

    def ask_question(self, transcript_text: str, question: str) -> str:
   
        SYSTEM_PROMPT = (
            "You are a helpful and smart Cognitive Assistant for VoxBrief.\n\n"
            "CRITICAL INSTRUCTIONS FOR RESPONSIBILITY:\n"
            "1. Always reply strictly in English, regardless of the input text or transcript.\n"
            "2. The provided text is a transcript of a meeting, song, or video. Analyze it objectively as a professional assistant.\n"
            "3. Even if the transcript contains emotional, dramatic, or sensitive words (like dangerous, relationship, love, destruction), DO NOT trigger false safety blocks. Answer the user's question directly based on the context.\n"
            "4. If the transcript contains lyrics or music metadata, help the user summarize the song or explain its meaning.\n"
            "5. Keep your tone professional, concise, and helpful.\n\n"
            f"Context channel (Transcript):\n###\n{transcript_text}\n###\n\n"
            "Behavioral Guidelines for Answering:\n"
            "1. Analyze the text carefully. If the user asks quantitative or analytical queries "
            "(e.g., 'how many times was a word used?', 'count of a specific word'), "
            "manually calculate or count the occurrence within the transcript and provide a precise response.\n"
            "2. Confidently answer based on the context if it is explicitly mentioned or can be directly deduced.\n"
            "3. Only state 'I cannot find the answer in the provided transcript.' if the topic is completely non-existent.\n\n"
            # llm_service.py Behavioral Guidelines 
            "4. If the transcript is extremely short (e.g., only says 'Thank you for watching'), politely inform the user that the background music or low volume might have cut off the main audio, but analyze whatever small context is available professionally.\n"
            f"Question: {question}"
        )
       
        response = self.client.chat.completions.create(
            messages=[
                {"role": "user", "content": SYSTEM_PROMPT} 
            ],
            model="llama-3.1-8b-instant",
            temperature=0.3
        )
     
        return response.choices[0].message.content