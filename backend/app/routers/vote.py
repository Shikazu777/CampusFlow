from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.vote import Vote
from app.models.post import Post

from app.schemas.vote import VoteRequest

router = APIRouter(
    prefix="/votes",
    tags=["Votes"]
)


@router.post("/")
def vote_post(
    request: VoteRequest,
    db: Session = Depends(get_db)
):
    existing_vote = (
        db.query(Vote)
        .filter(
            Vote.post_id == request.post_id,
            Vote.user_id == request.user_id
        )
        .first()
    )

    if existing_vote:
        raise HTTPException(
            status_code=400,
            detail="Already voted"
        )

    vote = Vote(
        post_id=request.post_id,
        user_id=request.user_id,
        vote_type=request.vote_type
    )

    db.add(vote)

    post = (
        db.query(Post)
        .filter(Post.id == request.post_id)
        .first()
    )

    if request.vote_type == "UP":
        post.upvotes += 1

    if request.vote_type == "DOWN":
        post.downvotes += 1

    db.commit()

    return {
        "message": "Vote recorded"
    }