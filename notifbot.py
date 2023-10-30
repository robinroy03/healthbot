"""
Bro, it works :)
"""
import telebot
from dotenv import load_dotenv

import db

import time
import os

load_dotenv()
bot = telebot.TeleBot(os.getenv("NOTIF_BOT_TOKEN"), parse_mode = None)

"""
db.get_notification_list() => get the top 5 people to send notifications to 
(the data will be sorted since it is sequentially entered)
"""

def send_queue_notifications():
    """
    Fetch the queue people from the db and send notification for the first 5
    """
    for user in db.get_notification_list():
        bot.send_message(user['telegram_id'], "You can come now")

while True:
    send_queue_notifications()
    time.sleep(5)
bot.infinity_polling()