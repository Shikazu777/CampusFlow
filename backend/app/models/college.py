from sqlalchemy import Column, Integer, String

from app.database.database import Base


class College(Base):
    __tablename__ = "colleges"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    domain = Column(String, unique=True, nullable=False)