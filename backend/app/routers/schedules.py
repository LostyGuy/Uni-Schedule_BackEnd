from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

router = APIRouter()

@router.put("/calendar_update_request", response_class=JSONResponse)
async def changes_to_calendar():
    """
    Handle a PUT request to update the calendar.
    """
    raise NotImplementedError

@router.get("/calendar_update_retrival", response_class=JSONResponse)
async def changes_from_calendars():
    """
    Retrieve calendar update changes.
    """
    raise NotImplementedError

@router.get("/weekly_schedule", response_class=JSONResponse)
async def weekly_schedule():
    """
    Retrieve the weekly schedule.
    """
    raise NotImplementedError