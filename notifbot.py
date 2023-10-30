"""
Bro, it works :)
"""
import telebot
from dotenv import load_dotenv

import db

import os

"""
db.get_first_appointment() => get the top 5 people to send notifications to 
(the data will be sorted since it is sequentially entered)
"""

def send_queue_notifications():
    """
    Fetch the queue people from the db and send notification to the next person in queue
    """    
    load_dotenv()
    bot = telebot.TeleBot(os.getenv("NOTIF_BOT_TOKEN"), parse_mode = None)
    for user in db.get_first_appointment():
        bot.send_message(user['telegram_id'], "You can meet the doctor now")

def send_message_to_warden(telegram_id: int):
    load_dotenv()
    bot = telebot.TeleBot(os.getenv("NOTIF_BOT_TOKEN"), parse_mode = None)
    # hardcoding Harish's telegram ID => he is the warden here for testing 
    patient = db.get_patient(telegram_id)
    bot.send_message(5454943365, f'Student {patient["name"]} from room {patient["room_no"]} is sick and has requested for food to be sent to their room')

def send_message_to_warden_ambulance(telegram_id: int):
    load_dotenv()
    bot = telebot.TeleBot(os.getenv("NOTIF_BOT_TOKEN"), parse_mode = None)
    # hardcoding Harish again as the warden and Robin as the ambulance driver here
    patient = db.get_patient(telegram_id)
    
    # message to the warden
    bot.send_message(5454943365, f'Student {patient["name"]} from room {patient["room_no"]} phone {patient["phone_no"]} is sick and has requested for ambulance')

    # message to the ambulance driver
    bot.send_message(751788076 , f'A student in {patient["block"]} block is sick and needs ambulance, please contact the warden and take the necessary steps')
    