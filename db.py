# IMPORTS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
import os

from datetime import datetime


# SETUP
load_dotenv()
client = MongoClient(os.getenv("ATLAS_URI"), server_api=ServerApi('1'))
db = client[os.getenv("DB_NAME")]
patients_collection = db["patients"]
appointment_qeuue_collection = db["appointment_queue"]


# FUNCTIONS
# Registrations
def patient_exists(telegram_id: int) -> bool:
    return patients_collection.count_documents({"telegram_id": telegram_id}) != 0

def create_patient(telegram_id: int) -> None:
    new_patient = {
        "telegram_id": telegram_id,
        "has_registered": False,
        "name": None,
        "age": None,
        "sex": None,
        "reg_no": None,
        "block": None,
        "room_no": None,
        "consultations": []
    }

    patients_collection.insert_one(new_patient)

def patient_has_registered(telegram_id: int) -> bool:
    patient = patients_collection.find_one({"telegram_id": telegram_id})
    return patient["has_registered"]

def register_patient(telegram_id: int, name: str, age: int, sex: str, reg_no: str, block: str, room_no: int) -> None:
    patients_collection.update_one(
        {"telegram_id": telegram_id},
        {"$set": {
            "has_registered": True,
            "name": name,
            "age": age,
            "sex": sex,
            "reg_no": reg_no,
            "block": block,
            "room_no": room_no
        }}
    )


# Appointments
def create_appointment(telegram_id: int) -> None:
    patient = patients_collection.find_one({"telegram_id": telegram_id})
    new_appointment = {
        "telegram_id": patient["telegram_id"],
        "name": patient["name"],
        "age": patient["age"],
        "time": datetime.now(),
        "is_active": True,
    }

    appointment_qeuue_collection.insert_one(new_appointment)

def close_appointment(telegram_id: int) -> None:
    appointment_qeuue_collection.update_one(
        {"telegram_id": telegram_id},
        {"$set": {"is_active": False}}
    )

def get_appointment_queue_size() -> int:
    return appointment_qeuue_collection.count_documents({})

def get_active_appointments(telegram_id: int) -> list:
    return appointment_qeuue_collection.find({"telegram_id": telegram_id, "is_active": True})