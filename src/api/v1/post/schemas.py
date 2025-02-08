from pydantic import BaseModel
from datetime import datetime


class PostCreate(BaseModel):
    title: str
    content: str

    class Config:
        from_attributes = True


class PostInDB(PostCreate):
    id: int
    created_at: datetime
    updated_at: datetime


class PostUpdate(BaseModel):
    title: str
    content: str

    