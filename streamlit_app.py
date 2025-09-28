import streamlit as st

st.title("Welcome to gameTrax")

selected_game = st.selectbox(label="Select your game", options=["Phase 10", "Skip-Bo", "Uno"])

if selected_game == 'Skip-Bo':
  st.image("https://www.pngfind.com/pngs/m/227-2273272_skip-bo-skip-bo-clipart-hd-png-download.png")
