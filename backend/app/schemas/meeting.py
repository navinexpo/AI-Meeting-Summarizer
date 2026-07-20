from pydantic import BaseModel
from typing import List
# Question request model for the meeting analysis endpoint
class QuestionRequest(BaseModel):
    transcript: str
    question: str
# Task model for action items in the meeting analysis response
class ActionItem(BaseModel):
    task: str
    owner: str
    deadline: str

class MeetingAnalysisResponse(BaseModel):
    id: str
    summary: str
    key_takeaways: List[str]
    action_items: List[ActionItem]