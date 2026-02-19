# SolarPredict
### "AI-Based Solar Power Output Prediction using Linear Regression"

## Project Overview
This project predicts solar power output using environmental parameters such as irradiation and temperature.

The system is built using Linear Regression and achieves high prediction accuracy.

## Dataset
- Solar Power Generation Data (Plant 1) – Kaggle

## Features Used:
- Irradiation
- Ambient Temperature
- Module Temperature

## Target:
- AC Power (converted to kW)
- Model Performance
- R² Score: ~0.98
- MAE: ~0.026 kW
- RMSE: ~0.055 kW
- Cross-Validation R²: ~0.978

## Capabilities
- Solar output prediction
- Performance evaluation
- Residual analysis
- Basic recommendation logic

## Streamlit UI
This project also includes an interactive Streamlit application.

To run locally:
- pip install streamlit
- streamlit run streamlit_app.py

The app allows users to:
- Input irradiation
- Input ambient temperature
- Input module temperature
- Get predicted solar output
- Receive performance recommendations

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Matplotlib
-Seaborn

## Social Impact
Helps institutions and homeowners estimate expected solar output and monitor efficiency.
