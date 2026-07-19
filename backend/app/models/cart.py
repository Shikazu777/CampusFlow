from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.database import Base


class Cart(Base):
    __tablename__ = "carts"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        index=True
    )

    stall_id = Column(
        Integer,
        ForeignKey("stalls.id"),
        index=True
    )

    status = Column(
        String,
        default="ACTIVE",
        index=True
    )