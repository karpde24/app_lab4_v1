from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Float
)
from sqlalchemy.orm import relationship
from models.session import Base


class Trip(Base):
    __tablename__ = 'trip'
    __table_args__ = {'schema': 'new_lab_4'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    start_time = Column(String(45), nullable=False)
    end_time = Column(String(45), nullable=False)
    price = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('new_lab_4.user.id'), nullable=False, index=True)
    driver_id = Column(Integer, ForeignKey('new_lab_4.driver.id'), nullable=False, index=True)

    user = relationship("User", back_populates="trips")
    driver = relationship("Driver", back_populates="trips")

    def __repr__(self):
        return (
            f"<Trip(id={self.id}, start_time='{self.start_time}', end_time='{self.end_time}', "
            f"price={self.price}, user_id={self.user_id}, driver_id={self.driver_id}, "
            f"user={self.user}, driver={self.driver})>"
        )