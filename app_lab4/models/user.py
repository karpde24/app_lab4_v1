from sqlalchemy import (
    Column,
    Date,
    Integer,
    String,
    Float
)
from sqlalchemy.orm import relationship
from models.session import Base
from datetime import datetime


# User Model
class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'schema': 'new_lab_4', 'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    phone_number = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False, index=True)
    registration_date = Column(Date, nullable=False, default=datetime.now().date())
    rating = Column(Float, nullable=False)

    trips = relationship("Trip", back_populates="user", lazy="selectin")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"