from typing import List

from pydantic import BaseModel
from datetime import datetime
from schemas.users import UserDTO
from schemas.drivers import DriverDTO


class TripBase(BaseModel):
    start_time: str
    end_time: str
    price: float

    class Config:
        from_attributes = True


class CreateTripDTO(TripBase):
    user_id: int
    driver_id: int


class TripLessDTO(TripBase):
    id: int


class TripDTO(TripBase):
    id: int
    user: UserDTO
    driver: DriverDTO


class UserWithTripDTO(UserDTO):
    trips: List[TripLessDTO]


class DriverWithTripDTO(DriverDTO):
    trips: List[TripLessDTO]