from fastapi import HTTPException

from app.models.user import User


def require_roles(
    user: User,
    allowed_roles: list[int]
):
    if user.role_id not in allowed_roles:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )