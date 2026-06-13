from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/send_push", response_class=JSONResponse)
async def send_notification():
    raise NotImplementedError