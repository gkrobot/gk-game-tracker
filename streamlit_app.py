import streamlit as st

st.title("Welcome to gameTrax")

st.write("Select your game")
st.selectbox(options=["Phase 10", "Skip-Bo", "Uno"])