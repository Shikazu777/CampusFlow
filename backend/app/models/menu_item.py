from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Float
from sqlalchemy import ForeignKey

from app.database.database import Base


class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=True
    )

    image_url = Column(
        String,
        nullable=True
    )

    price = Column(
        Float,
        nullable=False
    )

    offer_active = Column(
        Boolean,
        default=False
    )

    offer_price = Column(
        Float,
        nullable=True
    )

    stock = Column(
        Integer,
        default=0
    )

    is_available = Column(
        Boolean,
        default=True
    )

    stall_id = Column(
        Integer,
        ForeignKey("stalls.id")
    )