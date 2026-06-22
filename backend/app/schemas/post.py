from pydantic import BaseModel


class PostCreate(BaseModel):
    user_id: int
    title: str
    content: str