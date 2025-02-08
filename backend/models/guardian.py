from config.db import guardians_collection

class Guardian:
    def __init__(self, name, phone, email, password):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password

    def save(self):
        # Insert guardian into MongoDB
        guardian_data = {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "password": self.password,
        }
        guardians_collection.insert_one(guardian_data)
        return guardians_collection.find_one({"email": self.email})