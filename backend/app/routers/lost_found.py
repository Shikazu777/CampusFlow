from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.lost_found import LostFound
from app.models.user import User

router = APIRouter(
    prefix="/lost-found",
    tags=["Lost & Found"]
)

@router.post("/")
def create_item(
    item: dict,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.id == item["user_id"])
        .first()
    )

    new_item = LostFound(
        user_id=item["user_id"],
        college_id=user.college_id,
        title=item["title"],
        description=item["description"],
        category=item["category"],
        is_lost=item["is_lost"]
    )

    db.add(new_item)

    db.commit()

    db.refresh(new_item)

    return new_item

@router.get("/{user_id}")
def get_items(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    return (
        db.query(LostFound)
        .filter(
            LostFound.college_id == user.college_id
        )
        .all()
    )
    
    
@router.get("/search/{keyword}")
def search_lost_found(
    keyword: str,
    db: Session = Depends(get_db)
):
    return (
        db.query(LostFound)
        .filter(
            LostFound.title.ilike(f"%{keyword}%")
            |
            LostFound.description.ilike(f"%{keyword}%")
        )
        .all()
    )