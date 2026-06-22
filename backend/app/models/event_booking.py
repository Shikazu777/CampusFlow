from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database.database import Base


class EventBooking(Base):
    __tablename__ = "event_bookings"

    id = Column(
        Integer,
        primary_key=True
    )

    event_id = Column(
        Integer,
        ForeignKey("events.id")
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    ticket_qr = Column(
        String,
        unique=True
    )

    attendance_status = Column(
        String,
        default="BOOKED"
    )