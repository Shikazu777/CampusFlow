from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.stall import Stall

from app.schemas.stall import (
    StallCreate,
    StallResponse
)

router = APIRouter(
    prefix="/stalls",
    tags=["Stalls"]
)


@router.post(
    "/",
    response_model=StallResponse
)
def create_stall(
    stall: StallCreate,
    db: Session = Depends(get_db)
):
    new_stall = Stall(
        name=stall.name,
        block_id=stall.block_id
    )

    db.add(new_stall)

    db.commit()

    db.refresh(new_stall)

    return new_stall


@router.get(
    "/",
    response_model=list[StallResponse]
)
def get_stalls(
    db: Session = Depends(get_db)
):
    return db.query(Stall).all()