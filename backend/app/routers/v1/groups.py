from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/add_user", response_class=JSONResponse)
async def add_to_calendar_request():
    """
    Add a user to a calendar request.
    
    Note: This endpoint is not yet implemented.
    """
    raise NotImplementedError
