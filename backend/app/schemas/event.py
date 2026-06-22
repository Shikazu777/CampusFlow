from pydantic import BaseModel


class EventBookingRequest(BaseModel):
    event_id: int
    user_id: int


class EventScanRequest(BaseModel):
    ticket_qr: str


