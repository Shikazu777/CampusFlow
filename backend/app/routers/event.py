from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.event import Event
import uuid
from app.models.user import User
from app.schemas.event import EventBookingRequest, EventScanRequest, EventCreateRequest, EventMediaCreate
from app.models.event_booking import EventBooking
from app.models.notification import Notification
from app.models.event_media import EventMedia
from app.core.rbac import require_roles
from app.core.security import get_current_user, security


router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


@router.post("/")
def create_event(
    event: EventCreateRequest,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(
            User.id == event.organizer_user_id
        )
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    require_roles(3, 4)(user)
    
    new_event = Event(
        title=event.title,
        description=event.description,
        location=event.location,
        event_date=event.event_date,
        max_capacity=event.max_capacity,
        booking_required=event.booking_required,
        organizer_user_id=event.organizer_user_id
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return new_event


@router.get("/")
def get_events(
    db: Session = Depends(get_db)
):
    return db.query(Event).all()

@router.post("/book")
def book_event(
    request: EventBookingRequest,
    db: Session = Depends(get_db)
):
    booking = EventBooking(
        event_id=request.event_id,
        user_id=request.user_id,
        ticket_qr=str(uuid.uuid4()),
        attendance_status="BOOKED"
    )

    db.add(booking)
    
    db.add(
    Notification(
        user_id=request.user_id,
        message="Event booked successfully."
    )
)

    db.commit()

    db.refresh(booking)

    return booking

@router.get("/my-bookings/{user_id}")
def get_my_bookings(
    user_id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(EventBooking)
        .filter(EventBooking.user_id == user_id)
        .all()
    )

@router.post("/scan-ticket")
def scan_ticket(
    request: EventScanRequest,
    db: Session = Depends(get_db)
):
    booking = (
        db.query(EventBooking)
        .filter(
            EventBooking.ticket_qr == request.ticket_qr
        )
        .first()
    )

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    booking.attendance_status = "ATTENDED"

    user = (
    db.query(User)
    .filter(User.id == booking.user_id)
    .first()
    )

    user.coins += 5
    user.trust_score += 2

    db.commit()

    return {
        "booking_id": booking.id,
        "attendance_status": "ATTENDED"
    }
    
@router.post("/{event_id}/media")
def add_event_media(
    event_id: int,
    media: EventMediaCreate,
    db: Session = Depends(get_db)
):
    total_media = (
        db.query(EventMedia)
        .filter(
            EventMedia.event_id == event_id
        )
        .count()
    )

    if total_media >= 10:
        raise HTTPException(
            status_code=400,
            detail="Maximum 10 media files allowed"
        )

    new_media = EventMedia(
        event_id=event_id,
        media_url=media.media_url,
        media_type=media.media_type
    )

    db.add(new_media)

    db.commit()

    db.refresh(new_media)

    return new_media

@router.get("/{event_id}/media")
def get_event_media(
    event_id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(EventMedia)
        .filter(
            EventMedia.event_id == event_id
        )
        .all()
    )