from pydantic import BaseModel
from pydantic import EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    student_id: str
    college_id: int
    role_id: int


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    student_id: str
    college_id: int
    role_id: int
    coins: int
    trust_score: int

    model_config = {
        "from_attributes": True
    }