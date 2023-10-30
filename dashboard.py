"""
The streamlit UI for the health center personnels
"""

import streamlit as st
from streamlit_autorefresh import st_autorefresh

import db
import notifbot

st_autorefresh(2000)

def appointment_over(telegram_id: int, prescription: str):
    """
    A wrappper for db.close_appointment()
    takes inputs such as symptoms, medicines, number of days to take medicines, when all (mrng, evng, night)
    """
    db.close_appointment(telegram_id)
    notifbot.send_queue_notifications()

for appointment in db.get_active_appointments():
    with st.container():
        left, right = st.columns(2, gap = "small")
        with left:
            st.write("Name: ", appointment['name'])
            st.write("Age: ", appointment['age'])
            st.write("Phone Number: ", appointment['phone_no'])
            st.write("Time: ", appointment['time'])
        with right:
            with st.form(key = str(appointment['telegram_id'])):
                dr_input = st.text_input(label = "Enter the patient presciption", placeholder = "Enter here")
                submitted = st.form_submit_button("Submit")

                if submitted and dr_input != "":
                    appointment_over(appointment['telegram_id'], dr_input)
            # st.button("Appointment over", key = appointment['telegram_id'], on_click = db.close_appointment, args = (appointment['telegram_id'],))
