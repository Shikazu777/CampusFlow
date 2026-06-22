from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.favorite import Favorite

router = APIRouter(
    prefix="/favorites",
    tags=["Favorites"]
)


@router.post("/")
def add_favorite(
    favorite: dict,
    db: Session = Depends(get_db)
):
    new_favorite = Favorite(**favorite)

    db.add(new_favorite)

    db.commit()

    db.refresh(new_favorite)

    return new_favorite


@router.get("/{user_id}")
def get_favorites(
    user_id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(Favorite)
        .filter(Favorite.user_id == user_id)
        .all()
    )