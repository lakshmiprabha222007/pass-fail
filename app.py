import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("trained_pass_fail_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("📊 Pass / Fail Prediction App")

st.write("Pass if predicted value is 50 or above")

# Generic numeric input (NOT study hours)
value = st.number_input("Enter Input Value", step=1.0)

if st.button("Predict"):
    input_data = np.array([[value]])
    predicted_value = model.predict(input_data)[0]

    st.write(f"Predicted Value: {predicted_value:.2f}")

    if predicted_value >= 50:
        st.success("✅ PASS")
    else:
        st.error("❌ FAIL")
