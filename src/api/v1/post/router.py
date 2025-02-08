from fastapi import APIRouter, Depends
from .schemas import PostCreate, PostUpdate, PostInDB
from .service import PostService
from sqlalchemy.ext.asyncio.session import AsyncSession
from src.database import database

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/")
async def create_post(post: PostCreate, session: AsyncSession = Depends(database.get_session)):
    return await PostService.create_post(session, post)


@router.get("/{post_id}")
async def get_post(post_id: int, session: AsyncSession = Depends(database.get_session)):
    return await PostService.get_post(session, post_id)


@router.get("/")
async def get_posts(skip: int = 0, limit: int = 10, session: AsyncSession = Depends(database.get_session)):
    return await PostService.get_posts(session, skip, limit)


@router.put("/{post_id}")
async def update_post(post_id: int, updated_post: PostUpdate, session: AsyncSession = Depends(database.get_session)):
    return await PostService.update_post(session, post_id, updated_post)


@router.delete("/{post_id}")
async def delete_post(post_id: int, session: AsyncSession = Depends(database.get_session)):
    return await PostService.delete_post(session, post_id)

