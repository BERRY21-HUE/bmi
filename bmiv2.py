import streamlit as st
from function import *

st.title("BMI CALCULATOR")
st.header("AI Medical Guidance")
try:
    username = st.text_input("NAME:", placeholder="Betty")
    weight = st.number_input("Weight(kg):")
    height = st.number_input("Height(m - e.g. 1.89):")

    bmi_overall = weight / (height * height)
    st.subheader(f"{bmi_overall:.2f}")

    if bmi_overall < 18.5:
        ai(bmi_overall, username)
    elif (bmi_overall >= 18.5) and (bmi_overall <= 24.9):
        ai(bmi_overall, username)
    elif (bmi_overall >= 25) and (bmi_overall <= 29.9):
        ai(bmi_overall, username)
    elif bmi_overall >= 30:
        ai(bmi_overall, username)
    else:
        st.info("Invalid Input")

except ZeroDivisionError:
    st.info("Enter Your Values")
    st.subheader("An AI Medical Advise will Display here depending on your BMI.....")
