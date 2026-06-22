from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime

from datetime import datetime

from app.database.database import Base


class MarketplaceItem(Base):
    __tablename__ = "marketplace_items"

    id = Column(
        Integer,
        primary_key=True
    )

    seller_user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    college_id = Column(
        Integer,
        ForeignKey("colleges.id")
    )

    title = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=False
    )

    category = Column(
        String
    )

    price = Column(
        Float
    )

    status = Column(
        String,
        default="AVAILABLE"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )