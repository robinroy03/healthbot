"""
The streamlit UI for the health center personnels
"""

import streamlit as st
from streamlit_autorefresh import st_autorefresh

import db
import notifbot

st_autorefresh(2000)


st.markdown("""
# ```Health-Centre Queue 🏥```
Used by the doctor to monitor the queue for the health centre appointments and log their prescriptions
""")

with st.expander("Usage"):
    st.markdown("""
    ```
    Enter the patient's prescription using the following format:
                
    Symptoms:
    Symptom1
    Symptom2
                
    Medicines:
    Medicine1 number_of_days X-O-O
    Medicine2 number_of_days O-X-O

    Medicine Timings Format: \"Morning-Afternoon-Night\"
    X = Do not take medicine 
    O = Take Medicine
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
    notifbot.send_prescription(telegram_id, prescription)
    db.create_consultation(telegram_id, symptoms, prescription)
    db.close_appointment(telegram_id)
    notifbot.send_queue_notifications()

for patient in db.get_active_appointments():
    with st.container():
        left, right = st.columns(2, gap = "small")
        with left:
            st.write("Name: ", patient['name'])
            st.write("Age: ", patient['age'])
            st.write("Sex: ", patient['sex'])
            st.write("Phone Number: ", patient['phone_no'])
            st.write("Time: ", patient['time'])
        
        with right:
            with st.form(key = str(patient['telegram_id'])):
                dr_input = st.text_area(value="Symptoms: \n\nMedicines: ", label = "Enter the patient presciption", placeholder = "Enter here")
                submitted = st.form_submit_button("Submit")

                if submitted and dr_input != "":
                    appointment_over(patient['telegram_id'], dr_input)
