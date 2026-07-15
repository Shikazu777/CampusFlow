from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database.database import Base
from sqlalchemy import DateTime
from datetime import datetime
from datetime import timedelta


class Post(Base):
    __tablename__ = "posts"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
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
        default="ACTIVE"
    )
    
    college_id = Column(
    Integer,
    ForeignKey("colleges.id")
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    ) 
    
    created_at = Column(
    DateTime,
    default=datetime.utcnow
    )

    expires_at = Column(
    DateTime,
    default=lambda:
        datetime.utcnow() + timedelta(days=7)
    )
    
    created_at = Column(
    DateTime,
    default=datetime.utcnow
    )