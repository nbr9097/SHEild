from fastapi import APIRouter, HTTPException
from models.user import User
from models.guardian import Guardian
import bcrypt

router = APIRouter()

@router.post("/signup")
async def signup(username: str, phone: str, age: int, email: str, password: str, guardian_name: str, guardian_phone: str, guardian_email: str):
    # Create Guardian
    # guardian = Guardian(guardian_name, guardian_phone, guardian_email)
    # guardian_data = guardian.save()

    # Create User
    user = User(username, phone, age, email, password, guardian_name, guardian_phone, guardian_email)
    user.save()

    return {"message": "User created successfully"}

@router.post("/user/login")
async def login(email: str, password: str):
    user = User.find_by_email(email)
    print(user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not bcrypt.checkpw(password.encode("utf-8"), user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return {"message": "Login successful", "user": user}

@router.post("/guard/login")
async def login(email: str, password: str):
    user = User.find_gaurd_by_email(email)
    print(user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not bcrypt.checkpw(password.encode("utf-8"), user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return {"message": "Login successful", "user": user}