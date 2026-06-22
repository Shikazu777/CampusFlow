from pydantic import BaseModel


class BlockCreate(BaseModel):
    name: str
    college_id: int


class BlockResponse(BaseModel):
    id: int
    name: str
    college_id: int

    model_config = {
        "from_attributes": True
    }