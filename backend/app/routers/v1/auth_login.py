from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from backend.connection.connection import get_db as db_session

router = APIRouter()

@router.post("/login", response_class=JSONResponse)
async def user_login_request(username: str, password: str, device_name: str, ip_address: str, db_session):
    """
    Handle user login requests.
    
    Note: This endpoint is not yet implemented. 
    """
    
    #---- Get username, password, device name, ip address ----#

@router.post("/logout", response_class=JSONResponse)
async def logout_request():
    """
    Handle logout requests.

    Note: This endpoint is not yet implemented.
    """
    raise NotImplementedError