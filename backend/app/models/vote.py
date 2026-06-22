from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database.database import Base


class Vote(Base):
    __tablename__ = "votes"

    id = Column(
        Integer,
        primary_key=True
    )

    post_id = Column(
        Integer,
        ForeignKey("posts.id")
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    vote_type = Column(
        String
    )