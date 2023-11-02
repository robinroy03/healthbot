# IMPORTS
import pandas as pd
import streamlit as st
import db
from datetime import datetime, timedelta


# HELPER FUNCTIONS
def create_stats_dataframe() -> pd.DataFrame:
    '''
    Creates a dataframe from the past 30 days of consultations
    Columns: symptom, count, frequency
    '''
    data = {"symptom": [], "count": [], "frequency": []}

    last_30_days_patients = db.get_consultations_from_last_30_days()
    for patient in last_30_days_patients:
        for consultation in patient["consultations"]:
            if consultation["time"] > datetime.now() - timedelta(days=30):
                for symptom in consultation["symptoms"]:
                    if symptom in data["symptom"]:
                        index = data["symptom"].index(symptom)
                        data["count"][index] += 1
                        date = (consultation["time"] - datetime.now()).days
                        data["frequency"][index][date] += 1
                    else:
                        data["symptom"].append(symptom)
                        data["count"].append(1)
                        data["frequency"].append([0]*30)
                        date = (consultation["time"] - datetime.now()).days
                        data["frequency"][-1][date] += 1

    df = pd.DataFrame(data)
    return df[["symptom", "count", "frequency"]]


# PAGE RENDER
st.markdown("""
# ```Real-time Statistics 📈```
Monitor real-time cases of all the symptoms in the past 30 days to predict outbreaks
___
""")
df = create_stats_dataframe()
st.dataframe(
    df,
    column_config={
        "symptom": st.column_config.Column(label="Symptom", width=300),
        "count": st.column_config.Column(label="Total Count", width=100),
        "frequency": st.column_config.LineChartColumn("Day-wise Frequency (Last 30 Days)", y_min=0, y_max=10)
    },
    hide_index=True
)