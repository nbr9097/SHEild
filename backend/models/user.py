from config.db import users_collection
import bcrypt

class User:
    def __init__(self, username, phone, age, email, password, guardian_name, guardian_phone, guardian_email):
        self.username = username
        self.phone = phone
        self.age = age
        self.email = email
        self.password = password
        self.guardian_name = guardian_name
        self.guardian_phone = guardian_phone
        self.guardian_email = guardian_email
    def save(self):
        # Hash password
        hashed_password = bcrypt.hashpw(self.password.encode("utf-8"), bcrypt.gensalt())

        # Insert user into MongoDB
        user_data = {
            "username": self.username,
            "phone": self.phone,
            "age": self.age,
            "email": self.email,
            "guardian_name": self.guardian_name,
            "guardian_phone": self.guardian_phone,
            "guardian_email" : self.guardian_email,
            "password": hashed_password,
        }
        users_collection.insert_one(user_data)

    @staticmethod
    def find_by_email(email):
        return users_collection.find_one({"email": email}, {"_id": 0})
    
    @staticmethod
    def find_gaurd_by_email(guardian_email):
        return users_collection.find_one({"guardian_email": guardian_email}, {"_id": 0})