from fastapi import APIRouter, HTTPException
from src.database import MeetDocument  # updated name
from src.schemas.space_name import MeetDocumentSpaceNameUpdate

router = APIRouter()

@router.get("/document/{meet_key}/convo_history", response_model=str, tags=["llm"])
def get_convo_history(meet_key: str):
    document = MeetDocument.objects(meet_key=meet_key).first()
    if not document:
        raise HTTPException(status_code=404, detail="MeetDocument not found")
    return document.convo_history


@router.put("/document/{meet_key}/convo_history", response_model=str, tags=["llm"])
def update_convo_history(meet_key: str, update: MeetDocumentSpaceNameUpdate):
    document = MeetDocument.objects(meet_key=meet_key).first()
    if not document:
        raise HTTPException(status_code=404, detail="MeetDocument not found")
    document.convo_history = update.convo_history
    document.save()
    return "Success"
