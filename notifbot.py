#IMPORTS
import telebot
from dotenv import load_dotenv

import db

import os


# CONSTANTS
# Hard coding the telegram IDs of the warden and ambulance driver here for the time being
WARDEN_TELEGRAM_ID = 5454943365 # Harish
AMBULANCE_DRIVER_TELEGRAM_ID = 751788076 # Robin
COUNSELLOR_TELEGRAM_ID = 751788076 # Robin

# FUNCTIONS
def send_queue_notif() -> None:
    '''
    Sends notification to the next person in queue
    '''
    load_dotenv()
    bot = telebot.TeleBot(os.getenv("NOTIF_BOT_TOKEN"), parse_mode = None)
    for user in db.get_first_appointment():
        bot.send_message(user['telegram_id'], "You can meet the doctor now")

def send_food_req_notif_to_warden(telegram_id: int) -> None:
    '''
    Sends notification to the warden about details of student who is requesting for food to be delivered to their room
    '''
    load_dotenv()
    bot = telebot.TeleBot(os.getenv("NOTIF_BOT_TOKEN"), parse_mode = None)
    patient = db.get_patient(telegram_id)
    bot.send_message(WARDEN_TELEGRAM_ID, f'Student {patient["name"]} from room {patient["room_no"]} is sick and has requested for food to be sent to their room')

def send_ambulance_notif(telegram_id: int) -> None:
    '''
    Sends notification to the warden and ambulance driver about details of student who is requesting for ambulance
    '''
    load_dotenv()
    bot = telebot.TeleBot(os.getenv("NOTIF_BOT_TOKEN"), parse_mode = None)
    patient = db.get_patient(telegram_id)
    
    # Message to the warden
    bot.send_message(WARDEN_TELEGRAM_ID, f'Student {patient["name"]} from room: {patient["room_no"]} phone number: {patient["phone_no"]} is sick and has requested for ambulance')

    # Message to the ambulance driver
    bot.send_message(AMBULANCE_DRIVER_TELEGRAM_ID , f'A student in {patient["block"]} block is sick and has requested for the ambulance')

def send_appointment_notif_to_counsellor(telegram_id: int) -> None:
    '''
    Sends notification to counsellor regarding scheduled appointment
    '''
    load_dotenv()
    bot = telebot.TeleBot(os.getenv("NOTIF_BOT_TOKEN"), parse_mode = None)
    patient = db.get_patient(telegram_id)
    
    bot.send_message(COUNSELLOR_TELEGRAM_ID , f'Student {patient["name"]} has booked an appointment with you.')

def unparse_prescription(prescription: list) -> str:
    '''
    Unparses the prescription and returns a string in the following format:
    Here is your prescription:

    Medicine: <medicine-name>
    Days: <number-of-days>
    Timings: <morning> <afternoon> <night>

    .
    .
    .
    '''
    unparsed_prescription = ""
    medicine_time = {0: 'Morning', 1: 'Afternoon', 2: 'Night'}
    for medicine in prescription:
        unparsed_prescription += f"Medicine: {medicine['name']}\nDays: {medicine['days']}\nTimings: "
        for i in range(len(medicine['timings'])):
            time = medicine['timings'][i]
            if time == True:
                unparsed_prescription += medicine_time[i] + " "
        unparsed_prescription += "\n\n"
    return unparsed_prescription

def send_prescription_to_patient(telegram_id: int, prescription: list) -> None:
    '''
    Sends notification to patient regarding their prescription after their consultation
    '''
    load_dotenv()
    bot = telebot.TeleBot(os.getenv("NOTIF_BOT_TOKEN"), parse_mode = None)

    unparsed_prescription = unparse_prescription(prescription)
    bot.send_message(telegram_id, f"Here is your prescription\n\n{unparsed_prescription}")