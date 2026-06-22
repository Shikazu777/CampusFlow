from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.marketplace_item import MarketplaceItem
from app.models.user import User

router = APIRouter(
    prefix="/marketplace",
    tags=["Marketplace"]
)

@router.get("/{user_id}")
def get_marketplace(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    return (
        db.query(MarketplaceItem)
        .filter(
            MarketplaceItem.college_id
            == user.college_id
        )
        .all()
    )
    
@router.get("/{user_id}/category/{category}")
def get_by_category(
    user_id: int,
    category: str,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    return (
        db.query(MarketplaceItem)
        .filter(
            MarketplaceItem.college_id
            == user.college_id,
            MarketplaceItem.category == category
        )
        .all()
    )
    
@router.get("/search/{keyword}")
def search_marketplace(
    keyword: str,
    db: Session = Depends(get_db)
):
    return (
        db.query(MarketplaceItem)
        .filter(
            MarketplaceItem.title.ilike(f"%{keyword}%")
            |
            MarketplaceItem.description.ilike(f"%{keyword}%")
        )
        .all()
    )
    
@router.get("/{user_id}/filters")
def filter_marketplace(
    user_id: int,
    category: str = None,
    max_price: float = None,
    status: str = "AVAILABLE",
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    query = (
        db.query(MarketplaceItem)
        .filter(
            MarketplaceItem.college_id
            == user.college_id
        )
    )

    if category:
        query = query.filter(
            MarketplaceItem.category == category
        )

    if max_price:
        query = query.filter(
            MarketplaceItem.price <= max_price
        )

    if status:
        query = query.filter(
            MarketplaceItem.status == status
        )

    return query.all()