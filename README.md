🧠 End-to-End Stroke Prediction ML Streamlit App
📌 Project Overview

This is an end-to-end Machine Learning project that predicts the risk of stroke based on patient medical data.

The project covers:

Data Cleaning & EDA

Handling Imbalanced Dataset using SMOTE

Multiple Model Comparison

Hyperparameter Tuning using GridSearchCV

Pipeline Implementation

Model Saving using Joblib

Deployment using Streamlit Cloud

🌐 Live Deployment

🚀 This application is successfully deployed on Streamlit Cloud.

🔗 Live App:
https://your-app-name.streamlit.app

(Replace with your actual Streamlit app link)

The app allows users to:

Enter patient details

Predict stroke risk instantly

View probability score

Interact with a modern gradient UI

🛠️ Tech Stack

Language

Python

Libraries

pandas

numpy

scikit-learn

xgboost

imbalanced-learn (SMOTE)

matplotlib

seaborn

joblib

streamlit

⚙️ Machine Learning Workflow
1️⃣ Data Preprocessing

Removed unnecessary columns

Handled missing values (BMI median imputation)

OneHot Encoding for categorical features

Standard Scaling for numerical features

2️⃣ Imbalanced Data Handling

Applied SMOTE to balance minority stroke class

3️⃣ Models Implemented

Logistic Regression

Decision Tree

Random Forest

SVM

KNN

Naive Bayes

XGBoost

4️⃣ Model Evaluation Metrics

Accuracy

Precision

Recall

F1-Score

Confusion Matrix

5️⃣ Deployment

Best model selected based on F1-score

Saved using Joblib

Integrated into Streamlit app

Deployed on Streamlit Cloud

📂 Project Structure
Stroke_Prediction_Project/
│
├── data/
│   └── healthcare-dataset-stroke-data.csv
│
├── models/
│   └── stroke_best_model.joblib
│
├── notebooks/
│   └── stroke_training.ipynb
│
├── app.py
├── train.py
├── requirements.txt
└── README.md
▶️ Run Locally
pip install -r requirements.txt
streamlit run app.py


👩‍💻 Author

Nisha S
Aspiring Data Scientist | Machine Learning Enthusiast




