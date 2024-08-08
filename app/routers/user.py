from fastapi import APIRouter
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship("Task", back_populates="user")


router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get("/")
def all_users():
    return {"message": "All users"}

@router.get("/{user_id}")
def user_by_id(user_id: int):
    return {"message": f"User {user_id}"}

@router.post("/create")
def create_user():
    return {"message": "User created"}

@router.put("/update")
def update_user():
    return {"message": "User updated"}

@router.delete("/delete")
def delete_user():
    return {"message": "User deleted"}

