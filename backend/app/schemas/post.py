from pydantic import BaseModel
from typing import Optional


class PostCreate(BaseModel):
    """Schema for creating a post."""
    user_id: int
    title: str
    content: str


class PostImageCreate(BaseModel):
    """Schema for adding image to post."""
    post_id: int
    image_url: str
    caption: Optional[str] = None


class PostImageResponse(BaseModel):
    """Schema for post image response."""
    id: int
    post_id: int
    image_url: str
    caption: Optional[str]

    class Config:
        from_attributes = True


class PostResponse(BaseModel):
    """Schema for post response."""
    id: int
    user_id: int
    college_id: int
    title: str
    content: str

    class Config:
        from_attributes = True