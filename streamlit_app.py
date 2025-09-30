import streamlit as st

st.title("Welcome to gameTrax")

st.session_state.authenticated = False

if st.session_state.authenticated == True:
  
  game_options = [None, "Phase 10", "Skip-Bo", "Uno"]
  
  selected_game = st.selectbox(label="Select your game", options=game_options, index=0)
  
  if selected_game:
    st.info(f"You're playing {selected_game}!")

else:
  user_name = st.text_input(label="Enter username", autocomplete=username)
  password = st.text_input(label="Enter password", type=password, autocomplete=password)
  if user_name and password:
    if user_name == st.secrets.USER and password == st.secrets.PASSWORD:
        st.session_state.authenticated = True
