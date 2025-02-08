from fastapi import APIRouter, HTTPException
from config.db import users_collection, guardians_collection
from bson import ObjectId
import smtplib
from email.mime.text import MIMEText
import os

router = APIRouter()

@router.post("/send-alert")
async def send_alert(user_id: str, situation: str):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    guardian = guardians_collection.find_one({"_id": user["guardian_id"]})

    # Send email to guardian
    msg = MIMEText(f"Your child is in an unsafe situation: {situation}. Please take action immediately.")
    msg["Subject"] = "Emergency Alert"
    msg["From"] = os.getenv("EMAIL")
    msg["To"] = guardian["email"]

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(os.getenv("EMAIL"), os.getenv("EMAIL_PASSWORD"))
        server.sendmail(os.getenv("EMAIL"), guardian["email"], msg.as_string())

    return {"message": "Alert sent successfully"}