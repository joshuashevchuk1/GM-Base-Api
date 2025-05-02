from fastapi import APIRouter, HTTPException
from src.database import MeetDocument
from src.schemas.topic_name import MeetDocumentTopicNameUpdate

router = APIRouter()

@router.get("/document/{meet_key}/topic_name", response_model=str, tags=["Space"])
def get_topic_name(meet_key: str):
    document = MeetDocument.objects(meet_key=meet_key).first()
    if not document:
        raise HTTPException(status_code=404, detail="MeetDocument not found")
    return document.topic_name


@router.put("/document/{meet_key}/topic_name", response_model=str, tags=["Space"])
def update_topic_name(meet_key: str, update: MeetDocumentTopicNameUpdate):
    document = MeetDocument.objects(meet_key=meet_key).first()
    if not document:
        raise HTTPException(status_code=404, detail="MeetDocument not found")
    document.topic_name = update.topic_name
    document.save()
    return "Success"
