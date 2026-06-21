from fastapi import APIRouter
from backend.app.routers import auth_login, auth_qr, users, schedules, groups, notifications

router = APIRouter(prefix="/api/v2")