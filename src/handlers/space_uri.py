from fastapi import APIRouter, HTTPException
from src.database import MeetDocument
from src.schemas.space_uri import MeetDocumentSpaceUriUpdate

router = APIRouter()

@router.get("/document/{meet_key}/space_uri", response_model=str, tags=["Space"])
def get_space_uri(meet_key: str):
    document = MeetDocument.objects(meet_key=meet_key).first()
    if not document:
        raise HTTPException(status_code=404, detail="MeetDocument not found")
    return document.space_uri


@router.put("/document/{meet_key}/space_uri", response_model=str, tags=["Space"])
def update_space_uri(meet_key: str, update: MeetDocumentSpaceUriUpdate):
    document = MeetDocument.objects(meet_key=meet_key).first()
    if not document:
        raise HTTPException(status_code=404, detail="MeetDocument not found")
    document.space_uri = update.space_uri
    document.save()
    return "Success"
