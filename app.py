import streamlit as st
import pickle

st.title('Diabetes Prediction ')

model = pickle.load(open('diabetes.pkl', 'rb'))
gender_mapping = {'Male':0,'Female':1, 'Other':2}
gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
gender_numeric=gender_mapping[gender]
age = st.number_input('Age', 1, 100)
hypertension_mapping = {'Yes':1, 'No':0}
hypertension = st.selectbox('Hypertension', ['Yes', 'No'])
hypertension_numeric=hypertension_mapping[hypertension]
heart_disease_mapping = {'Yes':1, 'No':0}
heart_disease = st.selectbox('Heart Disease', ['Yes', 'No'])
heart_disease_numeric=heart_disease_mapping[heart_disease] 
bmi = st.number_input('BMI', 1, 100)
hbA1c_level = st.number_input('HbA1c Level', 1, 50)
blood_glucose_level = st.number_input('Blood Glucose Level', 1, 400)

if st.button('Predict'):
    input_data = [[gender_numeric, age, hypertension_numeric, heart_disease_numeric, bmi, hbA1c_level, blood_glucose_level]]
    prediction = model.predict(input_data)
    diabetes = {0: 'Negative', 1: 'Positive'}
    predicted_diabetes = diabetes[prediction[0]]
    st.success(f'Prediction: {predicted_diabetes}')
