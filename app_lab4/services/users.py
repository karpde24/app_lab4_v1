from typing import List, Optional
from sqlalchemy.orm import selectinload
from models.user import User
from models.trip import Trip
from models.session import SessionLocal
from werkzeug.exceptions import NotFound, BadRequest



class UsersService:
    @staticmethod
    def get_user_by_id(id: int) -> Optional[User]:
        """Fetch a user by ID."""
        with SessionLocal() as db:
            user = db.query(User).options(
                selectinload(User.trips).selectinload(Trip.user),
                selectinload(User.trips).selectinload(Trip.driver)
            ).filter(User.id == id).first()
        return user

    @staticmethod
    def get_all_users() -> List[User]:
        """Fetch all users."""
        with SessionLocal() as db:
            return db.query(User).all()

    @staticmethod
    def create_user(
        name: str,
        phone_number: str,
        email: str,
        rating: float
    ) -> User:
        """Create a new user."""
        with SessionLocal() as db:
            new_user = User(
                name=name,
                phone_number=phone_number,
                email=email,
                rating=rating
            )
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
        return new_user

    @staticmethod
    def update_user(
        id: int,
        name: str,
        phone_number: str,
        email: str,
        rating: float
    ) -> User:
        """
        Update a user by ID.
        :param id:
        :param name:
        :param phone_number:
        :param email:
        :param rating:
        :return:
        """
        with SessionLocal() as db:
            user = db.query(User).filter(User.id == id).first()
            if user:
                user.name = name
                user.phone_number = phone_number
                user.email = email
                user.rating = rating
                db.commit()
                db.refresh(user)
                return user
            else:
                raise NotFound(description=f"User with id {id} not found")

    @staticmethod
    def delete_user(id: int) -> None:
        """Delete a user by ID."""
        with SessionLocal() as db:
            user = db.query(User).filter(User.id == id).first()
            if user:
                db.delete(user)
                db.commit()
            else:
                raise NotFound(description=f"User with id {id} not found")
