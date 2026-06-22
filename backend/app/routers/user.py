from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.user import User

from app.schemas.user import UserCreate, UserResponse

from app.core.security import hash_password
from app.models.order import Order
from app.models.event_booking import EventBooking
from app.models.post import Post
from app.models.cart import Cart
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.menu_item import MenuItem


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    new_user = User(
    name=user.name,
    email=user.email,
    password_hash=hash_password(user.password),
    student_id=user.student_id,
    college_id=user.college_id,
    role_id=user.role_id
)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/", response_model=list[UserResponse])
def get_users(
    db: Session = Depends(get_db)
):
    return db.query(User).all()

@router.get("/{user_id}/dashboard")
def student_dashboard(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    total_orders = (
        db.query(Order)
        .filter(Order.user_id == user_id)
        .count()
    )

    total_events = (
        db.query(EventBooking)
        .filter(
            EventBooking.user_id == user_id,
            EventBooking.attendance_status == "ATTENDED"
        )
        .count()
    )

    total_posts = (
        db.query(Post)
        .filter(Post.user_id == user_id)
        .count()
    )

    return {
        "name": user.name,
        "coins": user.coins,
        "trust_score": user.trust_score,
        "total_orders": total_orders,
        "events_attended": total_events,
        "posts_created": total_posts
    }
    
@router.get("/{user_id}/analytics")
def student_analytics(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    orders = (
        db.query(Order)
        .filter(Order.user_id == user_id)
        .all()
    )

    total_spent = sum(
        order.total_amount for order in orders
    )

    total_orders = len(orders)

    total_coins = user.coins

    food_counter = {}

    for order in orders:

        order_items = (
            db.query(OrderItem)
            .filter(
                OrderItem.order_id == order.id
            )
            .all()
        )

        for item in order_items:

            menu_item = (
                db.query(MenuItem)
                .filter(
                    MenuItem.id == item.menu_item_id
                )
                .first()
            )

            if menu_item.name not in food_counter:
                food_counter[menu_item.name] = 0

            food_counter[menu_item.name] += item.quantity

    favorite_food = None

    if food_counter:
        favorite_food = max(
            food_counter,
            key=food_counter.get
        )

    return {
        "student_name": user.name,
        "trust_score": user.trust_score,
        "wallet_coins": total_coins,
        "total_orders": total_orders,
        "total_spent": total_spent,
        "favorite_food": favorite_food
    }