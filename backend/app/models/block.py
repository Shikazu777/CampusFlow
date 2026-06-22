from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database.database import Base


class Block(Base):
    __tablename__ = "blocks"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String,
        nullable=False
    )

    college_id = Column(
        Integer,
        ForeignKey("colleges.id")
    )