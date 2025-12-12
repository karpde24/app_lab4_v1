from pydantic import BaseModel
from datetime import date


class UserBase(BaseModel):
    name: str
    phone_number: str
    email: str
    rating: float

    class Config:
        from_attributes = True


class CreateUserDTO(UserBase):
    pass


class UserDTO(UserBase):
    id: int
    registration_date: date
