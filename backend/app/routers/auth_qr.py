from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

router = APIRouter()


#!---- Agains SOLID principles ----
@router.post("/send_qr_code", response_class=JSONResponse)
async def send_qr_code():
    """
    Send a QR code to the client.
    
    Note: This endpoint is not yet implemented.
    """
    raise NotImplementedError