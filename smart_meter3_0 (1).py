
#!pip install -q streamlit pyngrok

from pyngrok import ngrok

# Only run this ONCE (replace with your token)
ngrok.set_auth_token("2whAAMu9D6dCaeouOFkTzuI8GkB_3v6goQQWUPavogQHpQZ2W")

import joblib

# Save the trained model and scaler (if any)
joblib.dump(model, 'isolation_model.pkl')

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import joblib
# import numpy as np
# 
# # Load the model
# model = joblib.load("isolation_model.pkl")
# 
# st.title("🔍 Smart Energy Anomaly Detector")
# st.markdown("Enter the meter data below:")
# 
# # Input form
# season = st.selectbox("Season", ["Summer", "Winter", "Rainy"])
# month = st.slider("Month (1-12)", 1, 12, 6)
# peak_load = st.number_input("Peak Load (in kWh)", min_value=100.0, max_value=2000.0, step=10.0)
# avg_usage = st.number_input("Average Monthly Usage (in kWh)", min_value=10.0, max_value=2000.0, step=10.0)
# 
# # Predict
# if st.button("Check Usage"):
#     usage_ratio = avg_usage / peak_load
#     prediction = model.predict([[usage_ratio]])[0]
#     result = "🔴 Anomaly" if prediction == -1 else "🟢 Normal"
#     st.subheader(f"Result: {result}")
#

from pyngrok import conf, ngrok
import os
import time
import threading

# (Optional) Authenticate ngrok - paste your token if needed
conf.get_default().auth_token = "2whAAMu9D6dCaeouOFkTzuI8GkB_3v6goQQWUPavogQHpQZ2W"  # Only required first time

# Function to run Streamlit
def run_streamlit():
    os.system('streamlit run app.py')

# Start Streamlit in background
thread = threading.Thread(target=run_streamlit)
thread.start()

# Allow time to start
time.sleep(5)

# Create public URL
# Change is on this line: provide the port within the addr argument
public_url = ngrok.connect(addr="8501")
print("🔗 Your Streamlit app is live at:", public_url)

# prompt: download pkl file



