from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime

from datetime import datetime

from app.database.database import Base


class LostFound(Base):
    __tablename__ = "lost_found"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    college_id = Column(
        Integer,
        ForeignKey("colleges.id")
    )

    title = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=False
    )

    category = Column(
        String
    )

    status = Column(
        String,
        default="OPEN"
    )

    is_lost = Column(
        Boolean
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )