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

"""

@bot.message_handler(commands = ['start'])
def start(message):
    if not db.is_registered(message.id):
        bot.reply_to(message, "Please register yourself using /register")
    else:
        bot.reply_to(message, "welcome to healthbot, we are here to help you out :)")

@bot.messag_handler(commands = ['register'])
def register(message):
    bot.reply_to(message, "Welcome, we'll register right now")