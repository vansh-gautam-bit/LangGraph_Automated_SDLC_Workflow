Here's the `services.py` file based on the provided requirements and architecture:

```python
from typing import Optional
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from models import User, Data
from services.exceptions import (
    UserAlreadyExists,
    UserNotFound,
    DataNotFound,
    DataAlreadyExists,
    InvalidData,
)
from services.utils import get_current_user
from pydantic import ValidationError

class UserService:
    def get_user(self, db: Session, user_id: int) -> User:
        """Get a user by ID."""
        try:
            return db.query(User).filter(User.id == user_id).first()
        except SQLAlchemyError as e:
            raise UserNotFound from e

    def get_users(self, db: Session) -> list[User]:
        """Get all users."""
        try:
            return db.query(User).all()
        except SQLAlchemyError as e:
            raise UserNotFound from e

    def create_user(self, db: Session, user: UserCreate) -> User:
        """Create a new user."""
        try:
            db_user = User(
                username=user.username,
                email=user.email,
                password=user.password,
            )
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
        except IntegrityError as e:
            raise UserAlreadyExists from e
        except SQLAlchemyError as e:
            raise UserNotFound from e

    def update_user(self, db: Session, user_id: int, user: UserUpdate) -> User:
        """Update an existing user."""
        try:
            db_user = self.get_user(db, user_id)
            if db_user:
                if user.username:
                    db_user.username = user.username
                if user.email:
                    db_user.email = user.email
                if user.password:
                    db_user.password = user.password
                db.commit()
                db.refresh(db_user)
                return db_user
            else:
                raise UserNotFound
        except SQLAlchemyError as e:
            raise UserNotFound from e

    def delete_user(self, db: Session, user_id: int) -> None:
        """Delete a user."""
        try:
            db_user = self.get_user(db, user_id)
            if db_user:
                db.delete(db_user)
                db.commit()
        except SQLAlchemyError as e:
            raise UserNotFound from e

class DataService:
    def get_data(self, db: Session, data_id: int) -> Data:
        """Get data by ID."""
        try:
            return db.query(Data).filter(Data.id == data_id).first()
        except SQLAlchemyError as e:
            raise DataNotFound from e

    def get_data_by_user(self, db: Session, user_id: int) -> list[Data]:
        """Get data by user ID."""
        try:
            return db.query(Data).filter(Data.user_id == user_id).all()
        except SQLAlchemyError as e:
            raise DataNotFound from e

    def create_data(self, db: Session, data: DataCreate, user_id: int) -> Data:
        """Create new data."""
        try:
            db_data = Data(
                user_id=user_id,
                data=data.data,
            )
            db.add(db_data)
            db.commit()
            db.refresh(db_data)
            return db_data
        except IntegrityError as e:
            raise DataAlreadyExists from e
        except SQLAlchemyError as e:
            raise DataNotFound from e

    def update_data(self, db: Session, data_id: int, data: DataUpdate) -> Data:
        """Update existing data."""
        try:
            db_data = self.get_data(db, data_id)
            if db_data:
                if data.data:
                    db_data.data = data.data
                db.commit()
                db.refresh(db_data)
                return db_data
            else:
                raise DataNotFound
        except SQLAlchemyError as e:
            raise DataNotFound from e

    def delete_data(self, db: Session, data_id: int) -> None:
        """Delete data."""
        try:
            db_data = self.get_data(db, data_id)
            if db_data:
                db.delete(db_data)
                db.commit()
        except SQLAlchemyError as e:
            raise DataNotFound from e
```

This code defines the service layer for the user and data models. It includes methods for CRUD operations, and uses SQLAlchemy ORM to interact with the database. The code also includes proper type hints, descriptive method names, and follows clean architecture principles.

Note that this code does not include any FastAPI routes or Pydantic schemas, as per the requirements. It also does not include any error handling for invalid data, as that is handled by the Pydantic schemas.

You can use this service layer in your FastAPI application by importing the necessary services and using them to perform CRUD operations. For example:

```python
from fastapi import FastAPI
from services import UserService, DataService

app = FastAPI()

user_service = UserService()
data_service = DataService()

@app.get("/users/")
def get_users():
    return user_service.get_users(db=Session())

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return user_service.get_user(db=Session(), user_id=user_id)

@app.post("/users/")
def create_user(user: UserCreate):
    return user_service.create_user(db=Session(), user=user)

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    return user_service.update_user(db=Session(), user_id=user_id, user=user)

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    user_service.delete_user(db=Session(), user_id=user_id)

@app.get("/data/")
def get_data():
    return data_service.get_data_by_user(db=Session(), user_id=get_current_user())

@app.post("/data/")
def create_data(data: DataCreate):
    return data_service.create_data(db=Session(), data=data, user_id=get_current_user())

@app.put("/data/{data_id}")
def update_data(data_id: int, data: DataUpdate):
    return data_service.update_data(db=Session(), data_id=data_id, data=data)

@app.delete("/data/{data_id}")
def delete_data(data_id: int):
    data_service.delete_data(db=Session(), data_id=data_id)
```

This code uses the service layer to perform CRUD operations on the user and data models, and returns the results to the client.