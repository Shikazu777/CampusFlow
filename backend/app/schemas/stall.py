from pydantic import BaseModel


class StallCreate(BaseModel):
    name: str
    block_id: int


class StallResponse(BaseModel):
    id: int
    name: str
    block_id: int

    model_config = {
        "from_attributes": True
    }