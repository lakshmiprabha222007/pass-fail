import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("trained_pass_fail_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🔍 Pass / Fail Prediction App")

st.write("Enter the required input value to predict result")

# Generic input (NOT study hours)
value = st.number_input("Enter Input Value", step=1.0)

if st.button("Predict"):
    input_data = np.array([[value]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ PASS")
    else:
        st.error("❌ FAIL")
