import streamlit as st

st.title("Welcome to gameTrax")

selected_game = st.selectbox(label="Select your game", options=["Phase 10", "Skip-Bo", "Uno"])

if selected_game:
  st.info(f"You're playing {selected_game}!")
