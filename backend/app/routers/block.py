from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.block import Block

from app.schemas.block import (
    BlockCreate,
    BlockResponse
)


router = APIRouter(
    prefix="/blocks",
    tags=["Blocks"]
)


@router.post(
    "/",
    response_model=BlockResponse
)
def create_block(
    block: BlockCreate,
    db: Session = Depends(get_db)
):
    new_block = Block(
        name=block.name,
        college_id=block.college_id
    )

    db.add(new_block)

    db.commit()

    db.refresh(new_block)

    return new_block


@router.get(
    "/",
    response_model=list[BlockResponse]
)
def get_blocks(
    db: Session = Depends(get_db)
):
    return db.query(Block).all()