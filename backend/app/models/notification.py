from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.database import Base


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        index=True
    )

    message = Column(
        String
    )

    status = Column(
        String,
        default="UNREAD",
        index=True
    )