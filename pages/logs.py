# import streamlit as st

# import db

# with st.form("Input Form"):
#     search = st.text_input(label = "Enter the register number of student")
#     submitted = st.form_submit_button("Search")

#     if submitted and search != "":
#         pass

import streamlit as st

import db

with st.form("Input Form"):
    search = st.text_input(label = "Enter the register number of student")
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
        data = {"time": patient_data['consultations'][0]['time'], "symptoms": patient_data['consultations'][0]['symptoms'], "prescription": patient_data['consultations'][0]['prescription']}
        print(data)