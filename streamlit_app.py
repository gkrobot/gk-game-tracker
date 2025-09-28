import streamlit as st

st.title("Welcome to gameTrax")

selected_game = st.selectbox(label="Select your game", options=[None, "Phase 10", "Skip-Bo", "Uno"], default=None)

if selected_game:
  st.info(f"You're playing {selected_game}!")
