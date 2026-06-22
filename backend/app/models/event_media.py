from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database.database import Base


class EventMedia(Base):
    __tablename__ = "event_media"

    id = Column(
        Integer,
        primary_key=True
    )

    event_id = Column(
        Integer,
        ForeignKey("events.id")
    )

    media_url = Column(
        String,
        nullable=False
    )

    media_type = Column(
        String
    )