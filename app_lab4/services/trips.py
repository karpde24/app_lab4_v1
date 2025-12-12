# services/trips.py
from typing import List, Optional

from sqlalchemy.orm import selectinload

from models.trip import Trip
from models.session import SessionLocal
from werkzeug.exceptions import NotFound, BadRequest

class TripsService:
    @staticmethod
    def get_trip_by_id(id: int) -> Optional[Trip]:
        """Fetch a trip by ID."""
        with SessionLocal() as db:
            return db.query(Trip).options(selectinload(Trip.user), selectinload(Trip.driver)).filter(Trip.id == id).first()

    @staticmethod
    def get_all_trips() -> List[Trip]:
        """Fetch all trips."""
        with SessionLocal() as db:
            return db.query(Trip).options(selectinload(Trip.user), selectinload(Trip.driver)).all()

    def create_trip(
        self,
        start_time: str,
        end_time: str,
        price: float,
        user_id: int,
        driver_id: int,
    ) -> Trip:
        """Create a new trip."""
        with SessionLocal() as db:
            new_trip = Trip(
                start_time=start_time,
                end_time=end_time,
                price=price,
                user_id=user_id,
                driver_id=driver_id
            )
            db.add(new_trip)
            db.commit()
            db.refresh(new_trip)
            new_trip = self.get_trip_by_id(new_trip.id)
        return new_trip

    def update_trip(self, id: int, **kwargs) -> Trip:
        """Update a trip by ID."""
        with SessionLocal() as db:
            trip = db.query(Trip).filter(Trip.id == id).first()
            if not trip:
                raise NotFound(description=f"Trip with id {id} not found")
            for key, value in kwargs.items():
                setattr(trip, key, value)
            db.commit()
            db.refresh(trip)
            trip = self.get_trip_by_id(trip.id)
        return trip

    @staticmethod
    def delete_trip(id: int) -> None:
        """Delete a trip by ID."""
        with SessionLocal() as db:
            trip = db.query(Trip).filter(Trip.id == id).first()
            if trip:
                db.delete(trip)
                db.commit()
            else:
                raise NotFound(description=f"Trip with id {id} not found")