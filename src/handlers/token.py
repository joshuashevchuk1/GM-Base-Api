from fastapi import APIRouter, HTTPException, UploadFile, File
from src.database import MeetDocument  # Assuming updated name
from io import BytesIO

router = APIRouter()


# Upload a token
@router.post("/document/{meet_key}/token", response_model=str, tags=["Token"])
async def update_token(meet_key: str, file: UploadFile = File(...)):
    document = MeetDocument.objects(meet_key=meet_key).first()
    if not document:
        raise HTTPException(status_code=404, detail="MeetDocument not found")

    file_data = await file.read()

    document.token.put(BytesIO(file_data), filename=file.filename)
    document.save()

    return "File uploaded successfully"

# Update a token
@router.put("/document/{meet_key}/token", response_model=str, tags=["Token"])
async def update_token(meet_key: str, file: UploadFile = File(...)):
    document = MeetDocument.objects(meet_key=meet_key).first()
    if not document:
        raise HTTPException(status_code=404, detail="MeetDocument not found")

    file_data = await file.read()

    document.token.replace(BytesIO(file_data), filename=file.filename)
    document.save()

    return "File uploaded successfully"


# Retrieve the uploaded token
@router.get("/document/{meet_key}/token", tags=["Token"])
async def get_file(meet_key: str):
    document = MeetDocument.objects(meet_key=meet_key).first()
    if not document:
        raise HTTPException(status_code=404, detail="MeetDocument not found")

    if document.token:
        return document.token.read()  # Return the file content
    else:
        raise HTTPException(status_code=404, detail="token file not found")

# Delete the uploaded token
@router.delete("/document/{meet_key}/token", response_model=str, tags=["Token"])
async def delete_token(meet_key: str):
    document = MeetDocument.objects(meet_key=meet_key).first()
    if not document:
        raise HTTPException(status_code=404, detail="MeetDocument not found")

    if not document.token:
        raise HTTPException(status_code=404, detail="token file not found")

    document.token.delete()
    document.token = None
    document.save()

    return "token deleted successfully"
