import streamlit as st
import joblib
import pandas as pd


st.title("🤖 Risk Prediction")


st.write(
    """
    Enter customer information to estimate insurance risk.
    """
)


age = st.number_input(
    "Customer Age",
    min_value=18,
    max_value=100
)


premium = st.number_input(
    "Annual Premium",
    min_value=0
)


vehicle_age = st.number_input(
    "Vehicle Age",
    min_value=0
)


if st.button("Predict Risk"):

    input_data = pd.DataFrame(
        {
            "Age":[age],
            "Premium":[premium],
            "VehicleAge":[vehicle_age]
        }
    )


    st.subheader("Prediction Result")


    # Temporary output
    # Replace with your actual model later

    risk = "Medium Risk"


    st.success(
        f"Predicted Category: {risk}"
    )