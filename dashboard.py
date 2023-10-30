"""
The streamlit UI for the health center personnels
"""

import streamlit as st
from streamlit_autorefresh import st_autorefresh

import db
import notifbot

st_autorefresh(2000)

with st.sidebar:
    st.markdown("""
    Navigate using the given tabs
    """)

st.markdown("""
# ```HealthBot Dashboard🏥```
In this page, you're having the queue of patient(s), which will be populated as new patients apply.
""")

with st.expander("See the explanation on usage"):
    st.markdown("""
    ```
    In the left, enter the patient prescription following this:
    
    \"Morning-Afternoon-Night\"
    X = Do not take medicine 
    O = Take Medicine
                
    Symptoms:
    Symptom1
    Symptom2
                
    Medicines:
    Medicine1 number_of_days X-O-O
    Medicine2 number_of_days O-X-O
    ```
    """)

st.markdown("""
---
""")

def appointment_over(telegram_id: int, dr_input: str):
    """
    A wrappper for db.close_appointment()
    takes inputs such as symptoms, medicines, number of days to take medicines, when all (mrng, evng, night)
    """
    symptoms, prescription = dr_input.split("\n\n")
    symptoms = symptoms.split("\n")[1:]
    prescription = prescription.split("\n")[1:]
    prescription = [medicine.split() for medicine in prescription]
    prescription = [{"name": prescription[0], "days": int(prescription[1]), "timings": [True if x == "O" else False for x in prescription[2].split("-")]} for prescription in prescription]
    print(symptoms, prescription)
    db.create_consultation(telegram_id, symptoms, prescription)
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
                dr_input = st.text_area(value="Symptoms: \n\nMedicines: ", label = "Enter the patient presciption", placeholder = "Enter here")
                submitted = st.form_submit_button("Submit")

                if submitted and dr_input != "":
                    appointment_over(appointment['telegram_id'], dr_input)
            # st.button("Appointment over", key = appointment['telegram_id'], on_click = db.close_appointment, args = (appointment['telegram_id'],))
