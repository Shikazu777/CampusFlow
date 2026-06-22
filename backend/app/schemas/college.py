from pydantic import BaseModel


class CollegeCreate(BaseModel):
    name: str
    domain: str


class CollegeResponse(BaseModel):
    id: int
    name: str
    domain: str

    model_config = {
        "from_attributes": True
    }