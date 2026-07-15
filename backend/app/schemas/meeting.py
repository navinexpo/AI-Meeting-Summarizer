from pydantic import BaseModel
from typing import List

class QuestionRequest(BaseModel):
    transcript: str
    question: str

class ActionItem(BaseModel):
    task: str
    owner: str
    deadline: str
# Response model for meeting analysis
class MeetingAnalysisResponse(BaseModel):
    id: str
    summary: str
    key_takeaways: List[str]
    action_items: List[ActionItem]