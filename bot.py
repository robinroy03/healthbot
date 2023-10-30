import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, MenuButtonWebApp

from dotenv import load_dotenv
import os 

import db

load_dotenv()
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"), parse_mode = None)

"""
Helper functions in the db

patient_exists(telegram_id: int) => check if the user with the given id is registered in the database

# not now for the MVP
get_current_state(telegram_id: int) => get the current state of the user, right now the plan is it to be 
['registration', 'started'], ['registration', 'name'] (name is to be entered), ['registration', 'regno'], ['registration', 'phone'],
['registration', 'vitmail'], ['registration', 'hostel block'], ['registration', 'room number']

# for the mvp
patient_has_registered(telegram_id: int) => [true, false]
register_patient(message.text: str) => to store the user acc details for new registration
"""

ACTIONS = ['Schedule a doctor appointment', 'Call Ambulance', 'Schedule a counsellor appointment', 'Deliver food to room']
markup = ReplyKeyboardMarkup(row_width=1)
for i in ACTIONS:
    markup.add(KeyboardButton(i))

@bot.message_handler(commands = ['start'])
def start(message):
    if not db.patient_exists(message.chat.id):
        db.create_patient(message.chat.id)
        bot.reply_to(message, "Please register yourself using /register")
    else:
        bot.reply_to(message, "welcome to healthbot, we are here to help you out :)", reply_markup = markup)

@bot.message_handler(commands = ['register'])
def register(message):
    if db.patient_has_registered(message.chat.id):
        bot.reply_to(message, "You are already registed. You do not have to register again", reply_markup = markup)
    else:
        bot.reply_to(message, "Enter your Name, Age, Sex, Registration Number, Hostel Block, Room Number in seperate lines")

@bot.message_handler(func = lambda message: True)
def router(message):
    """
    This function routes the text messages appropriately - acts as a state machine
    """
    if not db.patient_has_registered(message.chat.id):
        # this response is then the name, reg, phone thing .., so plug it into db
        patient_details = [message.chat.id, *message.text.split("\n")]
        db.register_patient(*patient_details)
        bot.reply_to(message, "You've registered, continue using the app", reply_markup = markup)
    if message.text == "Schedule a doctor appointment":
        if not db.appointment_exists(message.chat.id):
            doctor_appointment(message)
        else:
            bot.reply_to(message, "You already have an appointment registered")

def doctor_appointment(message):
    bot.reply_to(message, "Ok, we'll proceed to schedule an appointment with the doctor")
    db.create_appointment(message.chat.id)

bot.infinity_polling()