from pydantic import BaseModel
from typing import Optional


class FavoriteCreate(BaseModel):
    """Schema for creating a favorite."""
    user_id: int
    menu_item_id: Optional[int] = None
    post_id: Optional[int] = None


class FavoriteResponse(BaseModel):
    """Schema for favorite response."""
    id: int
    user_id: int
    menu_item_id: Optional[int]
    post_id: Optional[int]

    class Config:
        from_attributes = True
