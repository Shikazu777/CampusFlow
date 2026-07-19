from sqlalchemy import Column, Integer, Float, String, ForeignKey, Index

from app.database.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        index=True
    )

    total_amount = Column(
        Float,
        default=0
    )

    status = Column(
        String,
        default="PENDING",
        index=True
    )

    qr_code = Column(
        String,
        unique=True,
        nullable=True
    )

    pickup_status = Column(
        String,
        default="PENDING",
        index=True
    )

    coins_used = Column(
        Integer,
        default=0
    )