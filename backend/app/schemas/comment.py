from pydantic import BaseModel


class CommentCreate(BaseModel):
    post_id: int
    user_id: int
    content: str