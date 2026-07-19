from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Index
from datetime import datetime, timedelta

from app.database.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        index=True
    )

    title = Column(
        String,
        nullable=False
    )

    content = Column(
        String,
        nullable=False
    )

    upvotes = Column(
        Integer,
        default=0
    )

    downvotes = Column(
        Integer,
        default=0
    )

    status = Column(
        String,
        default="ACTIVE",
        index=True
    )
    
    college_id = Column(
        Integer,
        ForeignKey("colleges.id"),
        index=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        index=True
    ) 
    
    expires_at = Column(
        DateTime,
        default=lambda:
            datetime.utcnow() + timedelta(days=7),
        index=True
    )