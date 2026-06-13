from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/login", response_class=JSONResponse)
async def user_login_request():
    raise NotImplementedError

# @router.get("/login_credentials", response_class=JSONResponse)
# async def user_login_approval():
#     raise NotImplementedError

@router.post("/logout", response_class=JSONResponse)
async def logout_request():
    raise NotImplementedError