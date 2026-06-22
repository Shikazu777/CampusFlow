from pydantic import BaseModel



class AddToCartRequest(BaseModel):
    user_id: int
    menu_item_id: int
    quantity: int = 1


class CartItemResponse(BaseModel):
    id: int
    menu_item_id: int
    quantity: int

    model_config = {
        "from_attributes": True
    }

    

class CheckoutRequest(BaseModel):
    coins_to_use: int = 0