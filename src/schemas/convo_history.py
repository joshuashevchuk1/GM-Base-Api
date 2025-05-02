from src.database.model import MeetDocument
from pydantic import BaseModel, Field

class MeetDocumentConvoHistoryUpdate(BaseModel):
    convo_history: str = Field(..., min_length=1)

def get_convo_history(meet_key: str) -> str:
    document = MeetDocument.objects.get(meet_key=meet_key)
    return document.convo_history

def put_convo_history(meet_key: str, update_data: MeetDocumentConvoHistoryUpdate) -> MeetDocument:
    document = MeetDocument.objects.get(meet_key=meet_key)
    document.convo_history = update_data.convo_history
    document.save()
    return document

