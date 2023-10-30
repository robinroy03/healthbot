import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, MenuButtonWebApp

from dotenv import load_dotenv
import os 

import db

load_dotenv()
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"), parse_mode = None)

"""
Helper functions in the db

is_registered(telegram_id: int) => check if the user with the given id is registered in the database

# not now for the MVP
get_current_state(telegram_id: int) => get the current state of the user, right now the plan is it to be 
['registration', 'started'], ['registration', 'name'] (name is to be entered), ['registration', 'regno'], ['registration', 'phone'],
['registration', 'vitmail'], ['registration', 'hostel block'], ['registration', 'room number']

# for the mvp
is_registering(telegram_id: int) => [true, false]
db.store_user_details(message.text: str) => to store the user acc details for new registration
"""

@bot.message_handler(commands = ['start'])
def start(message):
    if not db.is_registered(message.id):
        bot.reply_to(message, "Please register yourself using /register")
    else:
        bot.reply_to(message, "welcome to healthbot, we are here to help you out :)")

@bot.message_handler(commands = ['register'])
def register(message):
    if db.is_registered(message.id):
        bot.reply_to(message, "You are already registed. You do not have to register again")
    else:
        bot.reply_to(message, "Enter your name, registration number, phone, vit mail id, room number and block (A, B, C, D1, D2) on seperate lines")

bot.message_handler(func = lambda message: True)
def router(message):
    """
    This function routes the text messages appropriately - acts as a state machine
    """
    if db.is_registering(message.id):
        # this response is then the name, reg, phone thing .., so plug it into db
        db.store_user_details(message.text)

bot.infinity_polling()
