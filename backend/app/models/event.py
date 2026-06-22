from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey

from app.database.database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(
        Integer,
        primary_key=True
    )

    title = Column(
        String,
        nullable=False
    )

    description = Column(
        String
    )

    location = Column(
        String
    )

    event_date = Column(
        String
    )

    max_capacity = Column(
        Integer,
        default=100
    )

    booking_required = Column(
        Boolean,
        default=True
    )

    status = Column(
        String,
        default="OPEN"
    )

    organizer_user_id = Column(
        Integer,
        ForeignKey("users.id")
    )
    
    
