from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/add_user", response_class=JSONResponse)
async def add_to_calendar_request():
    raise NotImplementedError

@router.post("/qr_code_creation", response_class=JSONResponse)
async def qr_code_creation():
    raise NotImplementedError

#!---- Agains SOLID principles ----
@router.get("/send_qr_code", response_class=JSONResponse)
async def send_qr_code():
    raise NotImplementedError