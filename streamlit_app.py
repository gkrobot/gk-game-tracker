import streamlit as st

st.title("Welcome to gameTrax")

game_options = [None, "Phase 10", "Skip-Bo", "Uno"]

selected_game = st.selectbox(label="Select your game", options=game_options, index=0)

if selected_game:
  st.info(f"You're playing {selected_game}!")
