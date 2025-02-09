from typing import Annotated
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base
from datetime import datetime




idpk = Annotated[int, mapped_column(primary_key=True, index=True)]

CreatedAt = Annotated[datetime, mapped_column(server_default=text("TIMEZONE(('utc'), now())"))]
UpdatedAt = Annotated[datetime, mapped_column(server_default=text("TIMEZONE(('utc'), now())"), onupdate=datetime.utcnow)]



class PostModel(Base):
    __tablename__ = "posts"

    id: Mapped[idpk]
    title: Mapped[str] = mapped_column()
    content: Mapped[str] = mapped_column()
    created_at: Mapped[CreatedAt]
    updated_at: Mapped[UpdatedAt]
