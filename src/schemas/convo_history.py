from typing import List, Union, Literal
from pydantic import BaseModel, Field
from src.database.model import MeetDocument

class TextContent(BaseModel):
    type: Literal["text"]
    text: str

class Message(BaseModel):
    role: str
    content: Union[str, List[TextContent]]

class MeetDocumentConvoHistoryUpdate(BaseModel):
    convo_history: List[Message] = Field(..., min_items=1)

def get_convo_history(meet_key: str) -> str:
    document = MeetDocument.objects.get(meet_key=meet_key)
    return document.convo_history

def put_convo_history(meet_key: str, update_data: MeetDocumentConvoHistoryUpdate) -> MeetDocument:
    document = MeetDocument.objects.get(meet_key=meet_key)
    document.convo_history = update_data.convo_history
    document.save()
    return document

