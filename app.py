import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("trained_pass_fail_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🎓 Pass / Fail Prediction App")

st.write("Enter the number of study hours to predict Pass or Fail")

# User input
study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    step=0.5
)

if st.button("Predict"):
    input_data = np.array([[study_hours]])
    result = model.predict(input_data)

    if result[0] == 1:
        st.success("✅ Prediction: PASS")
    else:
        st.error("❌ Prediction: FAIL")
