from pydantic import BaseModel
from typing import Optional


class LostFoundCreate(BaseModel):
    """Schema for creating a lost/found item."""
    user_id: int
    title: str
    description: str
    category: str
    is_lost: bool


class LostFoundUpdate(BaseModel):
    """Schema for updating a lost/found item."""
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    is_found: Optional[bool] = None


class LostFoundResponse(BaseModel):
    """Schema for lost/found item response."""
    id: int
    user_id: int
    college_id: int
    title: str
    description: str
    category: str
    is_lost: bool
    is_found: bool

    class Config:
        from_attributes = True
