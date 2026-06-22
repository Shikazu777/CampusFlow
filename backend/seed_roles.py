from app.database.database import SessionLocal

from app.models.role import Role


db = SessionLocal()

roles = [
    "STUDENT",
    "CANTEEN_MANAGER",
    "EVENT_ORGANIZER",
    "ADMIN"
]

for role_name in roles:

    exists = (
        db.query(Role)
        .filter(Role.name == role_name)
        .first()
    )

    if not exists:

        db.add(
            Role(name=role_name)
        )

db.commit()

print("Roles seeded")