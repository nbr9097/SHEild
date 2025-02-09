from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models.user import User
from models.guardian import Guardian
import bcrypt

router = APIRouter()
class Signup(BaseModel):
    username: str
    phone: str
    age: int
    email: str
    password: str
    guardian_name: str
    guardian_phone: str
    guardian_email: str

@router.post("/signup")
async def signup(signup_data : Signup):
    # Create User
    user = User(signup_data.username, signup_data.phone, signup_data.age, signup_data.email, signup_data.password, signup_data.guardian_name, signup_data.guardian_phone, signup_data.guardian_email)
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
    # Set email as a cookie
        response.set_cookie(key="user_email", value=email, max_age=1800)  # 30 minutes

    return {"message": "Login successful", "user": user}

@router.post("/guard/login")
async def login(email: str, password: str):
    user = User.find_gaurd_by_email(email)
    print(user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        # Set email as a cookie
        response.set_cookie(key="guard_email", value=email, max_age=1800)  # 30 minutes

    if not bcrypt.checkpw(password.encode("utf-8"), user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return {"message": "Login successful", "user": user}