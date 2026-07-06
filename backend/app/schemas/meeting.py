from pydantic import BaseModel
from typing import List
# Question request model for asking questions about the meeting transcript
class QuestionRequest(BaseModel):
    transcript: str
    question: str
    # Action item model for representing tasks, owners, and deadlines in the meeting analysis response
class ActionItem(BaseModel):
    task: str
    owner: str
    deadline: str
# Model for the response of meeting analysis
class MeetingAnalysisResponse(BaseModel):
    id: str
    summary: str
    key_takeaways: List[str]
    action_items: List[ActionItem]