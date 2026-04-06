import streamlit as st

# Title
st.title("My First Streamlit App created by Pavan ABG")

# Text
st.write("Welcome! This app calculates the square of a number.")

# Slider
st.header("Select a Number")
number = st.slider("Pick a number", 0, 100, 25)

# Result
st.subheader("Result")
squared_number = number * number
st.write(f"The square of **{number}** is **{squared_number}**.")