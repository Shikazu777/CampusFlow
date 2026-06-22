from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.post import Post
from app.models.user import User
from app.models.post_image import PostImage

from app.schemas.post import PostCreate

from datetime import datetime


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.post("/")
def create_post(
    post: PostCreate,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.id == post.user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Only students, faculty and admins can post
    allowed_roles = [1, 4, 6]

    if user.role_id not in allowed_roles:
        raise HTTPException(
            status_code=403,
            detail="You are not allowed to create posts"
        )

    # Community timeout check
    if (
        user.community_timeout_until
        and
        user.community_timeout_until > datetime.utcnow()
    ):
        raise HTTPException(
            status_code=403,
            detail="Community timeout active"
        )

    # Daily post limit
    today_posts = (
        db.query(Post)
        .filter(
            Post.user_id == post.user_id,
            Post.created_at >= datetime.utcnow().replace(
                hour=0,
                minute=0,
                second=0,
                microsecond=0
            )
        )
        .count()
    )

    # Admin can post unlimited
    if user.role_id != 4 and today_posts >= 1:
        raise HTTPException(
            status_code=400,
            detail="You have already created a post today"
        )

    new_post = Post(
        user_id=post.user_id,
        college_id=user.college_id,
        title=post.title,
        content=post.content
    )

    db.add(new_post)

    db.commit()

    db.refresh(new_post)

    return new_post


@router.get("/")
def get_posts(
    db: Session = Depends(get_db)
):
    return (
        db.query(Post)
        .filter(
            Post.expires_at > datetime.utcnow()
        )
        .all()
    )


@router.get("/recent/{user_id}")
def recent_posts(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    return (
        db.query(Post)
        .filter(
            Post.college_id == user.college_id
        )
        .order_by(
            Post.created_at.desc()
        )
        .all()
    )


@router.get("/top/{user_id}")
def top_posts(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    posts = (
        db.query(Post)
        .filter(
            Post.college_id == user.college_id
        )
        .all()
    )

    posts.sort(
        key=lambda p:
        (p.upvotes - p.downvotes),
        reverse=True
    )

    return posts


@router.get("/search/{keyword}")
def search_posts(
    keyword: str,
    db: Session = Depends(get_db)
):
    return (
        db.query(Post)
        .filter(
            Post.title.ilike(f"%{keyword}%")
            |
            Post.content.ilike(f"%{keyword}%")
        )
        .all()
    )


@router.post("/{post_id}/images")
def add_post_image(
    post_id: int,
    image: dict,
    db: Session = Depends(get_db)
):
    image_count = (
        db.query(PostImage)
        .filter(
            PostImage.post_id == post_id
        )
        .count()
    )

    if image_count >= 3:
        raise HTTPException(
            status_code=400,
            detail="Maximum 3 images allowed"
        )

    new_image = PostImage(
        post_id=post_id,
        image_url=image["image_url"]
    )

    db.add(new_image)

    db.commit()

    db.refresh(new_image)

    return new_image


@router.get("/{post_id}/images")
def get_post_images(
    post_id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(PostImage)
        .filter(
            PostImage.post_id == post_id
        )
        .all()
    )