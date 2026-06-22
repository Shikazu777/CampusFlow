from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database.database import Base
from sqlalchemy import DateTime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    password_hash = Column(String, nullable=False)
    community_timeout_until = Column(
    DateTime,
    nullable=True
)

    student_id = Column(
        String,
        unique=True,
        nullable=False
    )

    college_id = Column(
        Integer,
        ForeignKey("colleges.id")
    )

    role_id = Column(
        Integer,
        ForeignKey("roles.id")
    )

    coins = Column(
    Integer,
    default=0
   )

    trust_score = Column(
    Integer,
    default=50
    )