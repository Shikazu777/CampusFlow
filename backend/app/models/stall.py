from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database.database import Base


class Stall(Base):
    __tablename__ = "stalls"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String,
        nullable=False
    )

    block_id = Column(
        Integer,
        ForeignKey("blocks.id")
    )

    editor_user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )