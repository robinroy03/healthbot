# IMPORTS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
import os


# SETUP
load_dotenv()
client = MongoClient(os.getenv("ATLAS_URI"), server_api=ServerApi('1'))
db = client[os.getenv("DB_NAME")]
consultations_collection = db["consultations"]


# FUNCTIONS
def get_consultations():
    return consultations_collection.find({})

for consultation in get_consultations():
    print(consultation)