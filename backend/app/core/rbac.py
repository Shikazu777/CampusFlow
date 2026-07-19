from fastapi import HTTPException, status
from app.models.user import User


ROLE_NAMES = {
    1: "STUDENT",
    2: "VENDOR",
    3: "ORGANIZER",
    4: "ADMIN",
    5: "STAFF",
    6: "FACULTY"
}


def require_roles(*allowed_role_ids: int):
    def role_checker(user: User):
        if user.role_id not in allowed_role_ids:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access denied. Required roles: {[ROLE_NAMES.get(rid, 'UNKNOWN') for rid in allowed_role_ids]}"
            )
        return user
    return role_checker