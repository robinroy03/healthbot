# IMPORTS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
import os


# SETUP
load_dotenv()
client = MongoClient(os.getenv("ATLAS_URI"), server_api=ServerApi('1'))
db = client[os.getenv("DB_NAME")]
patients_collection = db["patients"]


# FUNCTIONS
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