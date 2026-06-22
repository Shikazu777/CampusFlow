from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import ForeignKey

from app.database.database import Base


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(
        Integer,
        primary_key=True
    )

    order_id = Column(
        Integer,
        ForeignKey("orders.id")
    )

    menu_item_id = Column(
        Integer,
        ForeignKey("menu_items.id")
    )

    quantity = Column(
        Integer,
        default=1
    )

    price = Column(
        Float
    )