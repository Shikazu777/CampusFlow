from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import uuid

from app.database.database import get_db

from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.menu_item import MenuItem
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.user import User

from app.schemas.cart import AddToCartRequest, CheckoutRequest

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)


@router.post("/add-item")
def add_item(
    request: AddToCartRequest,
    db: Session = Depends(get_db)
):
    menu_item = (
        db.query(MenuItem)
        .filter(MenuItem.id == request.menu_item_id)
        .first()
    )

    if not menu_item:
        raise HTTPException(
            status_code=404,
            detail="Menu item not found"
        )

    cart = (
        db.query(Cart)
        .filter(
            Cart.user_id == request.user_id,
            Cart.stall_id == menu_item.stall_id,
            Cart.status == "ACTIVE"
        )
        .first()
    )

    if not cart:
        cart = Cart(
            user_id=request.user_id,
            stall_id=menu_item.stall_id,
            status="ACTIVE"
        )

        db.add(cart)
        db.commit()
        db.refresh(cart)

    cart_item = (
        db.query(CartItem)
        .filter(
            CartItem.cart_id == cart.id,
            CartItem.menu_item_id == menu_item.id
        )
        .first()
    )

    if cart_item:
        cart_item.quantity += request.quantity
    else:
        cart_item = CartItem(
            cart_id=cart.id,
            menu_item_id=menu_item.id,
            quantity=request.quantity
        )

        db.add(cart_item)

    db.commit()

    return {
        "message": "Item added to cart",
        "cart_id": cart.id
    }


@router.get("/my-carts/{user_id}")
def get_my_carts(
    user_id: int,
    db: Session = Depends(get_db)
):
    carts = (
        db.query(Cart)
        .filter(Cart.user_id == user_id)
        .all()
    )

    return carts


@router.post("/checkout/{cart_id}")
def checkout_cart(
    cart_id: int,
    request: CheckoutRequest,
    db: Session = Depends(get_db)
):
    cart = (
        db.query(Cart)
        .filter(Cart.id == cart_id)
        .first()
    )

    if not cart:
        raise HTTPException(
            status_code=404,
            detail="Cart not found"
        )

    items = (
        db.query(CartItem)
        .filter(CartItem.cart_id == cart.id)
        .all()
    )

    if not items:
        raise HTTPException(
            status_code=400,
            detail="Cart is empty"
        )

    total = 0

    for item in items:
        menu_item = (
            db.query(MenuItem)
            .filter(MenuItem.id == item.menu_item_id)
            .first()
        )

        if menu_item.stock < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"{menu_item.name} out of stock"
            )

        price = (
            menu_item.offer_price
            if menu_item.offer_active
            else menu_item.price
        )

        total += price * item.quantity

    user = (
        db.query(User)
        .filter(User.id == cart.user_id)
        .first()
    )

    coins_to_use = request.coins_to_use

    if coins_to_use > user.coins:
        coins_to_use = user.coins

    if coins_to_use > total:
        coins_to_use = int(total)

    final_amount = total - coins_to_use

    for item in items:
        menu_item = (
            db.query(MenuItem)
            .filter(MenuItem.id == item.menu_item_id)
            .first()
        )

        menu_item.stock -= item.quantity

    order = Order(
        user_id=cart.user_id,
        total_amount=final_amount,
        status="PENDING",
        qr_code=str(uuid.uuid4()),
        pickup_status="PENDING",
        coins_used=coins_to_use
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    for item in items:
        menu_item = (
            db.query(MenuItem)
            .filter(MenuItem.id == item.menu_item_id)
            .first()
        )

        price = (
            menu_item.offer_price
            if menu_item.offer_active
            else menu_item.price
        )

        db.add(
            OrderItem(
                order_id=order.id,
                menu_item_id=menu_item.id,
                quantity=item.quantity,
                price=price
            )
        )

    cart.status = "CHECKED_OUT"

    db.commit()

    return {
        "order_id": order.id,
        "original_amount": total,
        "coins_used": coins_to_use,
        "final_amount": final_amount,
        "status": order.status
    }

@router.get("/{cart_id}")
def get_cart_details(
    cart_id: int,
    db: Session = Depends(get_db)
):
    cart = (
        db.query(Cart)
        .filter(Cart.id == cart_id)
        .first()
    )

    if not cart:
        raise HTTPException(
            status_code=404,
            detail="Cart not found"
        )

    cart_items = (
        db.query(CartItem)
        .filter(
            CartItem.cart_id == cart.id
        )
        .all()
    )

    items = []

    total = 0

    for cart_item in cart_items:

        menu_item = (
            db.query(MenuItem)
            .filter(
                MenuItem.id ==
                cart_item.menu_item_id
            )
            .first()
        )

        price = (
            menu_item.offer_price
            if menu_item.offer_active
            else menu_item.price
        )

        subtotal = (
            price * cart_item.quantity
        )

        total += subtotal

        items.append(
            {
                "menu_item_id": menu_item.id,
                "name": menu_item.name,
                "price": price,
                "quantity": cart_item.quantity,
                "subtotal": subtotal
            }
        )

    return {
        "cart_id": cart.id,
        "status": cart.status,
        "items": items,
        "total": total
    }