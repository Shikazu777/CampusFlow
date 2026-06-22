from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.menu_item import MenuItem
from app.models.user import User
from fastapi import HTTPException
from app.models.notification import Notification

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.get("/my-orders/{user_id}")
def get_my_orders(
    user_id: int,
    db: Session = Depends(get_db)
):
    orders = (
        db.query(Order)
        .filter(Order.user_id == user_id)
        .all()
    )

    return orders



@router.get("/stall/{stall_id}")
def get_stall_orders(
    stall_id: int,
    db: Session = Depends(get_db)
):
    orders = db.query(Order).all()

    result = []

    for order in orders:

        order_items = (
            db.query(OrderItem)
            .filter(
                OrderItem.order_id == order.id
            )
            .all()
        )

        belongs_to_stall = False

        for item in order_items:

            menu_item = (
                db.query(MenuItem)
                .filter(
                    MenuItem.id == item.menu_item_id
                )
                .first()
            )

            if menu_item.stall_id == stall_id:
                belongs_to_stall = True
                break

        if belongs_to_stall:

            student = (
                db.query(User)
                .filter(
                    User.id == order.user_id
                )
                .first()
            )

            result.append(
                {
                    "order_id": order.id,
                    "student_name": student.name,
                    "total_amount": order.total_amount,
                    "status": order.status
                }
            )

    return result

@router.post("/{order_id}/ready")
def mark_order_ready(
    order_id: int,
    db: Session = Depends(get_db)
):
    order = (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    order.pickup_status = "READY"
    
    db.add(
    Notification(
        user_id=order.user_id,
        message="Your order is ready for pickup."
    )
)

    db.commit()

    return {
        "order_id": order.id,
        "pickup_status": order.pickup_status
    }

@router.get("/active-qrs/{user_id}")
def get_active_qrs(
    user_id: int,
    db: Session = Depends(get_db)
):
    orders = (
        db.query(Order)
        .filter(
            Order.user_id == user_id,
            Order.pickup_status != "COLLECTED"
        )
        .all()
    )

    return orders

from pydantic import BaseModel

class QRScanRequest(BaseModel):
    qr_code: str



@router.get("/{order_id}")
def get_order_details(
    order_id: int,
    db: Session = Depends(get_db)
):
    order = (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    order_items = (
        db.query(OrderItem)
        .filter(OrderItem.order_id == order.id)
        .all()
    )

    items = []

    for order_item in order_items:

        menu_item = (
            db.query(MenuItem)
            .filter(
                MenuItem.id == order_item.menu_item_id
            )
            .first()
        )

        items.append(
            {
                "menu_item_id": menu_item.id,
                "name": menu_item.name,
                "quantity": order_item.quantity,
                "price": order_item.price
            }
        )

    return {
        "order_id": order.id,
        "status": order.status,
        "total_amount": order.total_amount,
        "items": items
    }


@router.post("/scan")
def scan_qr(
    request: QRScanRequest,
    db: Session = Depends(get_db)
):
    order = (
        db.query(Order)
        .filter(Order.qr_code == request.qr_code)
        .first()
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="QR not found"
        )

    order.pickup_status = "COLLECTED"
    
    db.add(
    Notification(
        user_id=order.user_id,
        message="Your order has been collected."
    )
)

    db.commit()

    return {
        "order_id": order.id,
        "pickup_status": "COLLECTED"
    }
    
    
@router.post("/{order_id}/payment-success")
def payment_success(
    order_id: int,
    db: Session = Depends(get_db)
):
    order = (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    user = (
        db.query(User)
        .filter(User.id == order.user_id)
        .first()
    )

    if order.status == "PAID":
        raise HTTPException(
            status_code=400,
            detail="Already paid"
        )

    user.coins -= order.coins_used

    if user.coins < 0:
        user.coins = 0

    coins_earned = int(
        order.total_amount // 50
    ) * 2

    user.coins += coins_earned

    order.status = "PAID"
    
    db.add(
    Notification(
        user_id=user.id,
        message=f"You earned {coins_earned} coins from your order."
    )
)

    db.commit()

    return {
        "order_id": order.id,
        "coins_used": order.coins_used,
        "coins_earned": coins_earned,
        "pickup_status": order.pickup_status,
        "total_amount": order.total_amount,
        "qr_code": order.qr_code,
    }