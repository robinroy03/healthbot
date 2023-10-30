import streamlit as st

import db

with st.form("Input Form"):
    search = st.text_input(label = "Enter the register number of student")
    submitted = st.form_submit_button("Search")

    if submitted and search != "":
        pass