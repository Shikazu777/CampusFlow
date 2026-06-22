from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey

from app.database.database import Base


class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(
        Integer,
        primary_key=True
    )

    cart_id = Column(
        Integer,
        ForeignKey("carts.id")
    )

    menu_item_id = Column(
        Integer,
        ForeignKey("menu_items.id")
    )

    quantity = Column(
        Integer,
        default=1
    )