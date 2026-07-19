from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Index

from app.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False, index=True)

    password_hash = Column(String, nullable=False)
    
    community_timeout_until = Column(
        DateTime,
        nullable=True
    )

    student_id = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    college_id = Column(
        Integer,
        ForeignKey("colleges.id"),
        index=True
    )

    role_id = Column(
        Integer,
        ForeignKey("roles.id"),
        index=True
    )

    coins = Column(
        Integer,
        default=0
    )

    trust_score = Column(
        Integer,
        default=50
    )


__table_args__ = (
    Index('idx_user_college_role', 'college_id', 'role_id'),
)