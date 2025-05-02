from src.database.model import MeetDocument
from pydantic import BaseModel, Field

class MeetDocumentTopicNameUpdate(BaseModel):
    topic_name: str = Field(..., min_length=1)

def get_topic_name(meet_key: str) -> str:
    document = MeetDocument.objects.get(meet_key=meet_key)
    return document.topic_name

# UPDATE
def update_topic_name(meet_key: str, update_data: MeetDocumentTopicNameUpdate) -> MeetDocument:
    document = MeetDocument.objects.get(meet_key=meet_key)
    document.topic_name = update_data.topic_name
    document.save()
    return document
