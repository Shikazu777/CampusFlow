from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.menu_item import MenuItem

from app.schemas.menu_item import (
    MenuItemCreate,
    MenuItemResponse
)

router = APIRouter(
    prefix="/menu-items",
    tags=["Menu Items"]
)


@router.post(
    "/",
    response_model=MenuItemResponse
)
def create_menu_item(
    item: MenuItemCreate,
    db: Session = Depends(get_db)
):
    new_item = MenuItem(
        **item.model_dump()
    )

    db.add(new_item)

    db.commit()

    db.refresh(new_item)

    return new_item


@router.get(
    "/",
    response_model=list[MenuItemResponse]
)
def get_menu_items(
    db: Session = Depends(get_db)
):
    return db.query(MenuItem).all()