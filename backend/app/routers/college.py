from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.college import College

from app.schemas.college import CollegeCreate


router = APIRouter(
    prefix="/colleges",
    tags=["Colleges"]
)


@router.post("/")
def create_college(
    college: CollegeCreate,
    db: Session = Depends(get_db)
):
    new_college = College(
        name=college.name,
        domain=college.domain
    )

    db.add(new_college)

    db.commit()

    db.refresh(new_college)

    return new_college


@router.get("/")
def get_colleges(
    db: Session = Depends(get_db)
):
    return db.query(College).all()