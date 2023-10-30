"""
The streamlit UI for the health center personnels
"""

import streamlit as st
from streamlit_autorefresh import st_autorefresh
from streamlit_modal import Modal

import streamlit.components.v1 as components


import db

st_autorefresh(2000)

def appointment_over(telegram_id: int):
    """
    A wrappper for db.close_appointment() and for showing the modal message and take inputs such as
    symptoms, medicines, number of days to take medicines, when all (mrng, evng, night)
    """
    


for appointment in db.get_active_appointments():
    with st.container():
        left, right = st.columns(2, gap = "small")
        with left:
            st.write("Name:", appointment['name'])
            st.write("Age:", appointment['age'])
        with right:
            st.button("Appointment over", key = appointment['telegram_id'], on_click = db.close_appointment, args = (appointment['telegram_id'],))