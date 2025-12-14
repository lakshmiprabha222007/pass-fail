import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("trained_pass_fail_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("📊 Pass / Fail Prediction")

st.write("Enter study hours to predict result")

# Input from user
hours = st.number_input("Study Hours", 0.0, 24.0, step=0.5)

if st.button("Predict"):
    hours_input = np.array([[hours]])
    prediction = model.predict(hours_input)

    if prediction[0] == 1:
        st.success("✅ PASS")
    else:
        st.error("❌ FAIL")

