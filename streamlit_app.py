import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("solar_linear_regression_model.pkl")

st.title("SolarPredict - Solar Power Output Prediction System")

st.write("""
This tool predicts solar power output based on:
- Solar Irradiation
- Ambient Temperature
- Module Temperature
""")

# User Inputs
irradiation = st.slider("Irradiation (W/m²)", 0, 1200, 500)
ambient_temp = st.slider("Ambient Temperature (°C)", 0, 60, 30)
module_temp = st.slider("Module Temperature (°C)", 0, 80, 35)

# Predict Button
if st.button("Predict Solar Output"):

    input_df = pd.DataFrame({
        'IRRADIATION': [irradiation],
        'AMBIENT_TEMPERATURE': [ambient_temp],
        'MODULE_TEMPERATURE': [module_temp]
    })

    prediction = model.predict(input_df)[0]

    st.subheader(f"Predicted Solar Power Output: {prediction:.2f} kW")

    # Simple Recommendation Logic
    if irradiation > 800 and prediction < 0.5:
        st.warning("⚠️ Output lower than expected under high radiation. Inspect panels ⚠️")

    elif module_temp > 50:
        st.warning("⚠️ High module temperature may reduce efficiency ⚠️")

    elif irradiation < 200:
        st.info("ℹ️ Low sunlight conditions. Reduced output expected ℹ️")

    else:
        st.success("✅ System operating normally ✅")


