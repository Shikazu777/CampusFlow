from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.user import User
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.menu_item import MenuItem
from app.models.event import Event
from app.models.post import Post


router = APIRouter(
    prefix="/admin",
    tags=["Admin Analytics"]
)


@router.get("/analytics")
def admin_analytics(
    db: Session = Depends(get_db)
):
    total_students = (
        db.query(User).count()
    )

    total_orders = (
        db.query(Order).count()
    )

    total_events = (
        db.query(Event).count()
    )

    total_posts = (
        db.query(Post).count()
    )

    total_revenue = sum(
        order.total_amount
        for order in db.query(Order).all()
    )

    food_counter = {}

    order_items = db.query(OrderItem).all()

    for item in order_items:

        menu_item = (
            db.query(MenuItem)
            .filter(
                MenuItem.id == item.menu_item_id
            )
            .first()
        )

        if not menu_item:
            continue

        if menu_item.name not in food_counter:
            food_counter[menu_item.name] = 0

        food_counter[menu_item.name] += item.quantity

    most_popular_food = None

    if food_counter:
        most_popular_food = max(
            food_counter,
            key=food_counter.get
        )

    return {
        "total_students": total_students,
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "total_events": total_events,
        "total_posts": total_posts,
        "most_popular_food": most_popular_food
    }