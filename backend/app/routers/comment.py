from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.comment import Comment
from app.schemas.comment import CommentCreate

router = APIRouter(
    prefix="/comments",
    tags=["Comments"]
)


@router.post("/")
def create_comment(
    comment: CommentCreate,
    db: Session = Depends(get_db)
):
    new_comment = Comment(
        post_id=comment.post_id,
        user_id=comment.user_id,
        content=comment.content
    )

    db.add(new_comment)

    db.commit()

    db.refresh(new_comment)

    return new_comment


@router.get("/post/{post_id}")
def get_post_comments(
    post_id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(Comment)
        .filter(Comment.post_id == post_id)
        .all()
    )