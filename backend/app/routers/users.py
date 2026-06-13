from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/register", response_class=JSONResponse)
async def user_register_request():
    raise NotImplementedError

@router.get("/profile", response_class=JSONResponse)
async def get_user_profile():
    raise NotImplementedError

#delete
#update