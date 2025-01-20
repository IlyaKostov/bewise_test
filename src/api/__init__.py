__all__ = [
    'router'
]

from fastapi import APIRouter
from src.api.v1.application import router as applications

router = APIRouter()
router.include_router(applications, prefix='/v1', tags=['Application | v1'])
