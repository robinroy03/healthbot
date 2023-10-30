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
appointment_queue_collection = db["appointment_queue"]


# FUNCTIONS
# Registrations
def patient_exists(telegram_id: int) -> bool:
    '''
    Returns True if the patient exists in the database, False otherwise
    '''
    return patients_collection.count_documents({"telegram_id": telegram_id}) != 0

def create_patient(telegram_id: int) -> None:
    '''
    Creates a new empty patient in the database with empty fields
    '''
    new_patient = {
        "telegram_id": telegram_id,
        "has_registered": False,
        "is_sick": False,
        "name": None,
        "age": None,
        "sex": None,
        "reg_no": None,
        "block": None,
        "room_no": None,
        "phone_no": None,
        "consultations": []
    }

    patients_collection.insert_one(new_patient)

def get_patient(telegram_id: int) -> dict:
    '''
    Returns the patient with the given telegram_id
    '''
    return patients_collection.find_one({"telegram_id": telegram_id})

def patient_has_registered(telegram_id: int) -> bool:
    '''
    Returns True if the patient has registered (If the empty fields have been filled), False otherwise
    '''
    patient = get_patient(telegram_id)
    return patient["has_registered"]

def register_patient(telegram_id: int, name: str, age: int, sex: str, reg_no: str, block: str, room_no: int, phone_no: int) -> None:
    '''
    Fills the empty fields of the patient with the given details
    '''
    patients_collection.update_one(
        {"telegram_id": telegram_id},
        {"$set": {
            "has_registered": True,
            "name": name,
            "age": age,
            "sex": sex,
            "reg_no": reg_no,
            "block": block,
            "room_no": room_no,
            "phone_no": phone_no
        }}
    )

def make_patient_sick(telegram_id: int) -> None:
    '''
    Makes the patient with the given telegram_id sick
    '''
    patients_collection.update_one(
        {"telegram_id": telegram_id},
        {"$set": {"is_sick": True}}
    )

def get_sick_patients() -> list:
    '''
    Returns a list of all the sick patients
    '''
    return patients_collection.find({"is_sick": True})


# Appointments
def create_appointment(telegram_id: int) -> None:
    '''
    Creates a new appointment for the patient with the given telegram_id
    '''
    make_patient_sick(telegram_id)
    patient = get_patient(telegram_id)
    new_appointment = {
        "telegram_id": patient["telegram_id"],
        "name": patient["name"],
        "age": patient["age"],
        "phone_no": patient["phone_no"],
        "time": datetime.now(),
        "is_active": True,
    }

    appointment_queue_collection.insert_one(new_appointment)

def appointment_exists(telegram_id: int) -> bool:
    '''
    Returns True if the patient with the given telegram_id has an active appointment, False otherwise
    '''
    return appointment_queue_collection.count_documents({"telegram_id": telegram_id, "is_active": True}) != 0

def close_appointment(telegram_id: int) -> None:
    '''
    Closes the active appointment for the patient with the given telegram_id
    '''
    appointment_queue_collection.update_one(
        {"telegram_id": telegram_id, "is_active": True},
        {"$set": {"is_active": False}}
    )

def get_appointment_queue_size() -> int:
    '''
    Returns the number of active appointments
    '''
    return appointment_queue_collection.count_documents({})

def get_all_appointments() -> list:
    '''
    Returns a list of all the appointments
    '''
    return appointment_queue_collection.find({})

def get_active_appointments() -> list:
    '''
    Returns a list of all the active appointments for the patient with the given telegram_id
    '''
    return appointment_queue_collection.find({"is_active": True})

def get_first_appointment() -> list:
    '''
    Returns a list of the first three active appointments
    '''
    return appointment_queue_collection.find({"is_active": True}).limit(1)


# Consultations
def create_consultation(telegram_id: int, symptoms: list, prescription: dict) -> None:
    '''
    Creates a new consultation for the patient with the given telegram_id
    '''
    new_consultation = {
        "symptoms": symptoms,
        "prescription": prescription,
        "time": datetime.now()
    }
    patients_collection.update_one(
        {"telegram_id": telegram_id},
        {"$push": {"consultations": new_consultation}}
    )