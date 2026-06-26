from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from dotenv import load_dotenv

from backend.app.api.v1.routers import router
load_dotenv()

app = FastAPI()
app.include_router(router)

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
