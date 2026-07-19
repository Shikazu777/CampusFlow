from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.database import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(
        Integer,
        primary_key=True
    )

    post_id = Column(
        Integer,
        ForeignKey("posts.id"),
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        index=True
    )

    content = Column(
        String,
        nullable=False
    )