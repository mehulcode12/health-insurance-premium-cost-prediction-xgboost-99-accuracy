import streamlit as st
from prediction_helper import predict
from PIL import Image

# === Set up tabs ===
tab1, tab2, tab3 = st.tabs(["🔮 Prediction", "🧠 Model Accuracy (Age ≤ 25)", "🧠 Model Accuracy (Age > 25)"])

# === Tab 1: Prediction ===
with tab1:
    st.title('Health Insurance Cost Predictor')
    st.write('This app predicts the health insurance cost based on various factors.')
    st.write("Has an accuracy of 99% and less than 4% error.")

    categorical_options = {
        'Gender': ['Male', 'Female'],
        'Marital Status': ['Unmarried', 'Married'],
        'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
        'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
        'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
        'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
        'Medical History': [
            'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
            'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
            'Diabetes & Heart disease'
        ],
        'Insurance Plan': ['Bronze', 'Silver', 'Gold']
    }

    row1 = st.columns(3)
    row2 = st.columns(3)
    row3 = st.columns(3)
    row4 = st.columns(3)

    with row1[0]:
        age = st.number_input('Age', min_value=18, step=1, max_value=100)
    with row1[1]:
        number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
    with row1[2]:
        income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)

    with row2[0]:
        genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)
    with row2[1]:
        insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
    with row2[2]:
        employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

    with row3[0]:
        gender = st.selectbox('Gender', categorical_options['Gender'])
    with row3[1]:
        marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
    with row3[2]:
        bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])

    with row4[0]:
        smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
    with row4[1]:
        region = st.selectbox('Region', categorical_options['Region'])
    with row4[2]:
        medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

    input_dict = {
        'Age': age,
        'Number of Dependants': number_of_dependants,
        'Income in Lakhs': income_lakhs,
        'Genetical Risk': genetical_risk,
        'Insurance Plan': insurance_plan,
        'Employment Status': employment_status,
        'Gender': gender,
        'Marital Status': marital_status,
        'BMI Category': bmi_category,
        'Smoking Status': smoking_status,
        'Region': region,
        'Medical History': medical_history
    }

    if st.button('Predict'):
        prediction = predict(input_dict)
        st.success(f'Predicted Health Insurance Cost: {prediction}')

# === Tab 2: Model for Age ≤ 25 ===
with tab2:
    st.subheader("Model Performance: Age ≤ 25")
    st.image(Image.open("young_with_gr_accuracy.png"), caption="Linear Regression Accuracy")
    st.image(Image.open("young_with_gr_error.png"), caption="Residuals Distribution")

# === Tab 3: Model for Age > 25 ===
with tab3:
    st.subheader("Model Performance: Age > 25")
    st.image(Image.open("rest_with_gr_accuracy.png"), caption="XGBoost Accuracy")
    st.image(Image.open("rest_with_gr_error.png"), caption="Residuals Distribution")
