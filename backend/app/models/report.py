from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database.database import Base


class Report(Base):
    __tablename__ = "reports"

    id = Column(
        Integer,
        primary_key=True
    )

    post_id = Column(
        Integer,
        ForeignKey("posts.id")
    )

    reported_user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    reporter_user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    reason = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        default="PENDING"
    )