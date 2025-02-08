from fastapi import APIRouter
from src.api.v1.post.router import router as post_router

router = APIRouter(prefix="/v1")

router.include_router(post_router)