import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, MenuButtonWebApp

from dotenv import load_dotenv
import os 

import db
import notifbot

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

ACTIONS = ['Schedule a doctor\'s appointment', 'Call Ambulance', 'Schedule a counsellor appointment', 'Deliver food to room']
markup = ReplyKeyboardMarkup(row_width=1)
for i in ACTIONS:
    markup.add(KeyboardButton(i))

@bot.message_handler(commands = ['start'])
def start(message):
    if not db.patient_exists(message.chat.id):
        db.create_patient(message.chat.id)
        bot.reply_to(message, "Please register yourself using /register")
    else:
        bot.reply_to(message, "Welcome to healthbot, we are here to help you out :)", reply_markup = markup)

@bot.message_handler(commands = ['register'])
def register(message):
    if db.patient_has_registered(message.chat.id):
        bot.reply_to(message, "You are already registed. You do not have to register again", reply_markup = markup)
    else:
        bot.reply_to(message, '''Enter your details in the following format:\nName\nAge\nSex [M/F]\nRegistration Number\nHostel Block [A/B/C/D1/D2]\nRoom Number\nPhone Number''')

@bot.message_handler(func = lambda message: True)
def router(message):
    """
    This function routes the text messages appropriately - acts as a state machine
    """
    if not db.patient_has_registered(message.chat.id):
        # this response is then the name, reg, phone thing .., so plug it into db
        fields = message.text.split("\n")
        db.register_patient(message.chat.id, fields[0], int(fields[1]), fields[2], fields[3], fields[4], int(fields[5]), int(fields[6]))
        bot.reply_to(message, "You have registered, continue using the app", reply_markup = markup)
    if message.text == "Schedule a doctor's appointment":
        if not db.appointment_exists(message.chat.id):
            doctor_appointment(message)
        else:
            bot.reply_to(message, "You already have an appointment scheduled")
    elif message.text == "Deliver food to room":
        deliver_food_to_room(message)

def doctor_appointment(message):
    bot.reply_to(message, "Done! Your appointment has been scheduled")
    db.create_appointment(message.chat.id)

def deliver_food_to_room(message):
    if db.is_patient_sick(message.chat.id):
        bot.reply_to(message, "Done! We'll send food to your room soon :)")
        notifbot.send_message_to_warden(message.chat.id)
    else:
        bot.reply_to(message, "Sorry, you can't avail this feature when you're not sick")

bot.infinity_polling()