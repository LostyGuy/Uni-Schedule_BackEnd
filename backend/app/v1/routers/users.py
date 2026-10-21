from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

router = APIRouter()

#! ---- Possible User interactions ----
#? Create, Update, Delete User
#? Get User Profile
#? Get, Post User Setting - another router?
#? 

@router.post("/register", response_class=JSONResponse)
async def user_register_request():
    """
    Register a new user account.
    """
    raise NotImplementedError

@router.get("/profile", response_class=JSONResponse)
async def get_user_profile():
    """
    Retrieve the user's profile information.
    
    Returns:
    	JSONResponse: The authenticated user's profile data.
    """
    raise NotImplementedError

@router.post("/update", response_class=JSONResponse)
async def user_update_request():
    """
    Register a new user account.
    """
    raise NotImplementedError

@router.post("/delete", response_class=JSONResponse)
async def user_delete_request():
    """
    Register a new user account.
    """
    raise NotImplementedError

