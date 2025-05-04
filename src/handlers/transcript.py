from fastapi import APIRouter, HTTPException, UploadFile, File
from src.database import MeetDocument  # Assuming updated name
from io import BytesIO

router = APIRouter()


# Upload a transcript
@router.post("/document/{meet_key}/transcript", response_model=str, tags=["Transcript"])
async def post_transcript(meet_key: str, file: UploadFile = File(...)):
    document = MeetDocument.objects(meet_key=meet_key).first()
    if not document:
        raise HTTPException(status_code=404, detail="MeetDocument not found")

    file_data = await file.read()

    document.transcript.put(BytesIO(file_data), filename=file.filename)
    document.save()

    return "File uploaded successfully"

# Update a transcript
@router.put("/document/{meet_key}/transcript", response_model=str, tags=["Transcript"])
async def put_transcript(meet_key: str, file: UploadFile = File(...)):
    document = MeetDocument.objects(meet_key=meet_key).first()
    if not document:
        raise HTTPException(status_code=404, detail="MeetDocument not found")

    file_data = await file.read()

    document.transcript.replace(BytesIO(file_data), filename=file.filename)
    document.save()

    return "File uploaded successfully"


# Retrieve the uploaded transcript
@router.get("/document/{meet_key}/transcript", tags=["Transcript"])
async def get_file(meet_key: str):
    document = MeetDocument.objects(meet_key=meet_key).first()
    if not document:
        raise HTTPException(status_code=404, detail="MeetDocument not found")

    if document.transcript:
        return document.transcript.read()  # Return the file content
    else:
        raise HTTPException(status_code=404, detail="Transcript file not found")

# Delete the uploaded transcript
@router.delete("/document/{meet_key}/transcript", response_model=str, tags=["Transcript"])
async def delete_transcript(meet_key: str):
    document = MeetDocument.objects(meet_key=meet_key).first()
    if not document:
        raise HTTPException(status_code=404, detail="MeetDocument not found")

    if not document.transcript:
        raise HTTPException(status_code=404, detail="Transcript file not found")

    document.transcript.delete()
    document.transcript = None
    document.save()

    return "Transcript deleted successfully"
