from pydantic import BaseModel


class MenuItemCreate(BaseModel):
    name: str
    description: str | None = None
    image_url: str | None = None
    price: float
    offer_active: bool = False
    offer_price: float | None = None
    stock: int = 0
    is_available: bool = True
    stall_id: int


class MenuItemResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    image_url: str | None = None
    price: float
    offer_active: bool
    offer_price: float | None = None
    stock: int
    is_available: bool
    stall_id: int

    model_config = {
        "from_attributes": True
    }