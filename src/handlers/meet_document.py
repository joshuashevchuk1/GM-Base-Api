from fastapi import APIRouter, HTTPException
from src.database import MeetDocument
from src.schemas.meet_document import MeetDocumentCreate

router = APIRouter()

@router.post("/document", response_model=dict, tags=["Document"])
def create_document(doc: MeetDocumentCreate):
    if MeetDocument.objects(meet_key=doc.meet_key).first():
        raise HTTPException(status_code=400, detail="MeetDocument with this meet_key already exists")
    meet_doc = MeetDocument(**doc.dict())
    meet_doc.save()
    return {"created": True}

@router.delete("/document/{meet_key}", response_model=dict, tags=["Document"])
def delete_document(meet_key: str):
    space = MeetDocument.objects(meet_key=meet_key).first()
    if not space:
        raise HTTPException(status_code=404, detail="MeetDocument not found")
    space.delete()
    return {"deleted": True}