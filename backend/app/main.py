from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from dotenv import load_dotenv

from backend.app.routers import auth, groups, notifications, users, schedules
load_dotenv()

app = FastAPI()
app.include_router(auth.router, prefix="/auth")
app.include_router(groups.router, prefix="/groups")
app.include_router(notifications.router, prefix="/notifications")
app.include_router(users.router, prefix="/users")
app.include_router(schedules.router, prefix="/schedules")

#----For Web----
@app.get("/", response_class=JSONResponse)
async def main_page():
    """
    Return a greeting message from the root endpoint.
    
    Returns:
        dict: Dictionary containing the greeting {"Hello": "Hello World"}
    """
    return {"Hello":"Hello World"}
#----End For Web----
