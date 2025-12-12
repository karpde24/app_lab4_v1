from typing import List, Optional
from models.driver import Driver
from models.session import SessionLocal
from werkzeug.exceptions import NotFound, BadRequest


class DriversService:
    @staticmethod
    def get_driver_by_id(id: int) -> Optional[Driver]:
        """Fetch a driver by ID."""
        with SessionLocal() as db:
            return db.query(Driver).filter(Driver.id == id).first()

    @staticmethod
    def get_all_drivers() -> List[Driver]:
        """Fetch all drivers."""
        with SessionLocal() as db:
            return db.query(Driver).all()

    @staticmethod
    def create_driver(
        name: str,
        licence_number: str,
        phone_number: str,
        rating: str,
        experince_years: float,
        status: str
    ) -> Driver:
        """Create a new driver."""
        with SessionLocal() as db:
            new_driver = Driver(
                name=name,
                licence_number=licence_number,
                phone_number=phone_number,
                rating=rating,
                experince_years=experince_years,
                status=status
            )
            db.add(new_driver)
            db.commit()
            db.refresh(new_driver)
        return new_driver

    @staticmethod
    def update_driver(
        id: int,
        name: str,
        licence_number: str,
        phone_number: str,
        rating: str,
        experince_years: float,
        status: str
    ) -> Driver:
        """Update a driver."""
        with SessionLocal() as db:
            driver = db.query(Driver).filter(Driver.id == id).first()
            if driver:
                driver.name = name
                driver.licence_number = licence_number
                driver.phone_number = phone_number
                driver.rating = rating
                driver.experince_years = experince_years
                driver.status = status
                db.commit()
                db.refresh(driver)
                return driver
            else:
                raise NotFound(description=f"Driver with id {id} not found")

    @staticmethod
    def delete_driver(id: int) -> None:
        """Delete a driver by ID."""
        with SessionLocal() as db:
            driver = db.query(Driver).filter(Driver.id == id).first()
            if driver:
                db.delete(driver)
                db.commit()
            else:
                raise NotFound(description=f"Driver with id {id} not found")
