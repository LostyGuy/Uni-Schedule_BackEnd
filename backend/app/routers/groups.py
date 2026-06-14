from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/add_user", response_class=JSONResponse)
async def add_to_calendar_request():
    """
    Add a user to a calendar request.
    
    Raises:
    	NotImplementedError: This endpoint is not yet implemented.
    """
    raise NotImplementedError

@router.post("/qr_code_creation", response_class=JSONResponse)
async def qr_code_creation():
    """
    Create a QR code.
    """
    raise NotImplementedError

#!---- Agains SOLID principles ----
@router.get("/send_qr_code", response_class=JSONResponse)
async def send_qr_code():
    """
    Send a QR code to the client.
    
    Note: This endpoint is not yet implemented.
    """
    raise NotImplementedError