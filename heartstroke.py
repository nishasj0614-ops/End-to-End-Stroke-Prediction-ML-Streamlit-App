# =====================================================
# 🧠 Stroke Prediction Streamlit App
# =====================================================

import streamlit as st
import pandas as pd
import joblib

# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------
st.set_page_config(
    page_title="Stroke Prediction App",
    page_icon="🧠",
    layout="centered"
)

# -----------------------------------------------------
# Custom CSS Styling
# -----------------------------------------------------
st.markdown("""
<style>

/* Background Gradient */
.stApp {
    background: linear-gradient(135deg, #ffb6d9, #cfcfcf);
    background-attachment: fixed;
}

/* Main Card */
.main {
    background-color: rgba(255,255,255,0.9);
    padding: 2rem;
    border-radius: 20px;
}

/* Gradient Button */
div.stButton > button {
    background: linear-gradient(90deg, #ff1493, #808080);
    color: white;
    border: none;
    padding: 0.7rem 2rem;
    border-radius: 30px;
    font-size: 18px;
    font-weight: bold;
    transition: all 0.3s ease;
}

/* Button Hover */
div.stButton > button:hover {
    background: linear-gradient(90deg, #ff69b4, #555555);
    transform: scale(1.07);
    box-shadow: 0px 6px 20px rgba(0,0,0,0.3);
}

/* Result Box */
.result-box {
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    margin-top: 20px;
}

/* High Risk */
.high-risk {
    background: linear-gradient(90deg, #ff4d4d, #990000);
    color: white;
}

/* Low Risk */
.low-risk {
    background: linear-gradient(90deg, #00cc66, #006633);
    color: white;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# Load Trained Model
# -----------------------------------------------------
model = joblib.load("stroke_best_model.joblib")

# -----------------------------------------------------
# Title
# -----------------------------------------------------
st.title("🧠 Stroke Prediction App")
st.write("### Enter Patient Medical Details")

# -----------------------------------------------------
# Input Fields
# -----------------------------------------------------
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.number_input("Age", 1, 120)
hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])
ever_married = st.selectbox("Ever Married", ["Yes", "No"])
work_type = st.selectbox("Work Type",
                         ["Private", "Self-employed", "Govt_job",
                          "children", "Never_worked"])
residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])
avg_glucose_level = st.number_input("Average Glucose Level")
bmi = st.number_input("BMI")
smoking_status = st.selectbox("Smoking Status",
                              ["formerly smoked", "never smoked",
                               "smokes", "Unknown"])

# -----------------------------------------------------
# Prediction Button
# -----------------------------------------------------
if st.button("🔍 Predict Stroke Risk"):

    input_data = pd.DataFrame([{
        "gender": gender,
        "age": age,
        "hypertension": hypertension,
        "heart_disease": heart_disease,
        "ever_married": ever_married,
        "work_type": work_type,
        "Residence_type": residence_type,
        "avg_glucose_level": avg_glucose_level,
        "bmi": bmi,
        "smoking_status": smoking_status
    }])

    prediction = model.predict(input_data)[0]

    # Check if model supports probability
    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(input_data)[0][1]
    else:
        probability = 0.0

    if prediction == 1:
        st.markdown(
            f'<div class="result-box high-risk">'
            f'⚠ HIGH RISK of Stroke<br><br>'
            f'Risk Probability: {probability:.2%}'
            f'</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="result-box low-risk">'
            f'✅ LOW RISK of Stroke<br><br>'
            f'Risk Probability: {probability:.2%}'
            f'</div>',
            unsafe_allow_html=True
        )