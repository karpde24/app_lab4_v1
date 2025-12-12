from sqlalchemy import (
    Column,
    Integer,
    String,
    Float
)
from sqlalchemy.orm import relationship
from models.session import Base


# Driver Model
class Driver(Base):
    __tablename__ = 'driver'
    __table_args__ = {'schema': 'new_lab_4'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    licence_number = Column(String(45), nullable=False)
    phone_number = Column(String(45), nullable=False, index=True)  # Indexed
    rating = Column(String(45), nullable=False)
    experince_years = Column(Float, nullable=False)
    status = Column(String(45), nullable=False)

    trips = relationship("Trip", back_populates="driver", lazy="selectin")

    def __repr__(self):
        return (
            f"<Driver(id={self.id}, name='{self.name}', licence_number='{self.licence_number}', phone_number='{self.phone_number}', rating='{self.rating}', experince_years={self.experince_years}, status='{self.status}')>"
        )