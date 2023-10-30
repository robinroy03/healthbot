import streamlit as st

import db

import pandas as pd


with st.form("Input Form"):
    search = st.text_input(label = "Enter the register number of the patient: ")
    submitted = st.form_submit_button("Search")

if submitted and search != "":
    patient_data = db.get_patient_by_reg_no(search.upper())
    st.markdown(f"""```
Name: {patient_data['name']}
Registration Number: {patient_data['reg_no']}
Age: {patient_data['age']}
Sex: {patient_data['sex']}
Room Number: {patient_data['block']} - {patient_data['room_no']}
Phone Number: {patient_data['phone_no']}
```""")

    # Populating a datafram table with all previous consultations history
    for consultation in patient_data["consultations"]:
        time = consultation["time"]

        consultation["symptoms"] = ", ".join(consultation["symptoms"])

        prescription_strings = []
        for prescription in consultation["prescription"]:
            name = prescription['name']
            days = prescription['days']
            timings = prescription['timings']
            
            # Convert True and False values to 'O' and 'X'
            timings_str = '-'.join(['O' if t else 'X' for t in timings])
            
            prescription_string = f"{name} {days}x[{timings_str}]"
            prescription_strings.append(prescription_string)

        result = ', '.join(prescription_strings)

        consultation["prescription"] = result

    df = pd.DataFrame(patient_data["consultations"])
    st.dataframe(
        df[["time", "symptoms", "prescription"]],
        width=1000,
        hide_index=True
    )