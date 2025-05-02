from fastapi import APIRouter, HTTPException
from src.database import MeetDocument  # mongoengine document

router = APIRouter()

# DELETE a meet space by meet_key
@router.delete("/space/{meet_key}", response_model=dict, tags=["Document"])
def delete_space(meet_key: str):
    space = MeetDocument.objects(meet_key=meet_key).first()
    if not space:
        raise HTTPException(status_code=404, detail="MeetSpace not found")
    space.delete()
    return {"deleted": True}