from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database.database import Base


class PostImage(Base):
    __tablename__ = "post_images"

    id = Column(
        Integer,
        primary_key=True
    )

    post_id = Column(
        Integer,
        ForeignKey("posts.id")
    )

    image_url = Column(
        String,
        nullable=False
    )