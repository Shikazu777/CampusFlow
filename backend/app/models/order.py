from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    total_amount = Column(
        Float,
        default=0
    )

    status = Column(
        String,
        default="PENDING"
    )

    qr_code = Column(
    String,
    unique=True,
    nullable=True
    )

    pickup_status = Column(
    String,
    default="PENDING"
    )

    coins_used = Column(
    Integer,
    default=0
   )
        