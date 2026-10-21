from fastapi import APIRouter
from backend.app.v1.routers import auth_login, auth_qr, groups, notifications
from backend.app.v1.routers import users
from backend.app.v1.routers import schedules

router = APIRouter(prefix="/api/v1")

#* ----AUTHORIFICATION----
router.include_router(auth_login.router, prefix="/auth/session")
router.include_router(auth_qr.router, prefix="/auth/qr")

#* ----USERS----
router.include_router(users.router, prefix="/users")

#* ----SCHEDULES----
router.include_router(schedules.router, prefix="/schedules")

#* ----GROUPS----
router.include_router(groups.router, prefix="/groups")

#* ----NOTIFICATIONS----
router.include_router(notifications.router, prefix="/notifications")