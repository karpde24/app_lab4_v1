from pydantic import BaseModel


class DriverBase(BaseModel):
    name: str
    licence_number: str
    phone_number: str
    rating: str
    experince_years: float
    status: str

    class Config:
        from_attributes = True


class CreateDriverDTO(DriverBase):
    pass


class DriverDTO(DriverBase):
    id: int
