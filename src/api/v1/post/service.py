from fastapi import HTTPException
from sqlalchemy import select
from .model import PostModel
from .schemas import PostCreate, PostUpdate, PostInDB
from sqlalchemy.ext.asyncio.session import AsyncSession
from .exeptions import PostExeption

class PostService:
    @staticmethod
    async def create_post(session: AsyncSession, post: PostCreate):
        try:
            new_post = PostModel(**post.model_dump())
            session.add(new_post)
            await session.commit()
            await session.refresh(new_post)

            new_post = PostInDB.model_validate(new_post, from_attributes=True).model_dump()

            return {
                "message": "Post created successfully",
                "data": new_post
            }
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    @staticmethod
    async def get_post(session: AsyncSession, post_id: int):
        post = await session.get(PostModel, post_id)
        if post is None:
            raise PostExeption.PostNotFound()
        
        post = PostInDB.model_validate(post).model_dump()

        return {
            "message": "Post retrieved successfully",
            "data": post
        }
    
    @staticmethod
    async def get_posts(session: AsyncSession, skip: int = 0, limit: int = 10):
        try:
            stmt = select(PostModel).offset(skip).limit(limit)
            result = await session.execute(stmt)
            posts = result.scalars().all()

            posts = [PostInDB.model_validate(post).model_dump() for post in posts]

            return {
                "message": "Posts retrieved successfully",
                "data": posts
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    

    @staticmethod
    async def update_post(session: AsyncSession, post_id: int, updated_post: PostUpdate):
        post = await session.get(PostModel, post_id)
        if post is None:
            raise PostExeption.PostNotFound()
        
        for key, value in updated_post.model_dump(exclude_unset=True).items():
            setattr(post, key, value)

        await session.commit()
        await session.refresh(post)

        post = PostInDB.model_validate(post, from_attributes=True).model_dump()

        return {
            "message": "Post updated successfully",
            "data": post
        }
    
    @staticmethod
    async def delete_post(session: AsyncSession, post_id: int):
        post = await session.get(PostModel, post_id)
        if post is None:
            raise PostExeption.PostNotFound()
        
        await session.delete(post)
        await session.commit()
        return {
            "message": "Post deleted successfully"
        }