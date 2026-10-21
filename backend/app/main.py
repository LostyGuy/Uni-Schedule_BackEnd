from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from dotenv import load_dotenv

from backend.app.v1.api.routers import router
from backend.app.v1.error_handling import capture_errors
load_dotenv()

app = FastAPI()
app.include_router(router)
capture_errors(app)

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
