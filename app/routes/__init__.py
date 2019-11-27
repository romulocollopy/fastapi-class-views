from fastapi import APIRouter
from .home import router as home_router
from .echo import router as echo_router

router = APIRouter()
router.include_router(home_router)
router.include_router(echo_router)
