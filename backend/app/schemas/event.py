from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EventCreateRequest(BaseModel):
    """Schema for creating an event."""
    title: str
    description: str
    location: str
    event_date: datetime
    max_capacity: int = 100
    booking_required: bool = True
    organizer_user_id: int


class EventBookingRequest(BaseModel):
    """Schema for booking an event."""
    event_id: int
    user_id: int


class EventScanRequest(BaseModel):
    """Schema for scanning event ticket."""
    ticket_qr: str


class EventMediaCreate(BaseModel):
    """Schema for adding media to event."""
    event_id: int
    media_url: str
    media_type: str  # 'image' or 'video'


class EventMediaResponse(BaseModel):
    """Schema for event media response."""
    id: int
    event_id: int
    media_url: str
    media_type: str

    class Config:
        from_attributes = True
