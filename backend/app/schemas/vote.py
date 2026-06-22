from pydantic import BaseModel


class VoteRequest(BaseModel):
    post_id: int
    user_id: int
    vote_type: str