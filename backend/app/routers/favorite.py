from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.favorite import Favorite
from app.schemas.favorite import FavoriteCreate, FavoriteResponse

router = APIRouter(
    prefix="/favorites",
    tags=["Favorites"]
)


@router.post("/")
def add_favorite(
    favorite: FavoriteCreate,
    db: Session = Depends(get_db)
):
    new_favorite = Favorite(
        user_id=favorite.user_id,
        menu_item_id=favorite.menu_item_id,
        post_id=favorite.post_id
    )

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