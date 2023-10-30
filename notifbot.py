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
    Fetch the queue people from the db and send notification for the first 5
    """    
    load_dotenv()
    bot = telebot.TeleBot(os.getenv("NOTIF_BOT_TOKEN"), parse_mode = None)
    for user in db.get_first_appointment():
        bot.send_message(user['telegram_id'], "You can come now")

def send_message_to_warden(telegram_id: int):
    load_dotenv()
    bot = telebot.TeleBot(os.getenv("NOTIF_BOT_TOKEN"), parse_mode = None)
    # hardcoding Harish's telegram ID => he is the warden here for testing 
    bot.send_message(5454943365, f"Student {db.get_patient(telegram_id).values()} is sick and needs food to his room")