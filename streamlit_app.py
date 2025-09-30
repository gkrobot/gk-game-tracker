import streamlit as st
import time

st.title("Welcome to gameTrax")

if 'authenticated' not in st.session_state:
  st.session_state.authenticated = False

if st.session_state.authenticated == True:
  
  game_options = [None, "Phase 10", "Skip-Bo", "Uno"]
  
  selected_game = st.selectbox(label="Select your game", options=game_options, index=0)
  
  if selected_game:
    st.info(f"You're playing {selected_game}!")

else:
  user_name = st.text_input(label="Enter username", autocomplete="username")
  password = st.text_input(label="Enter password", type="password", autocomplete="current-password")
  if user_name and password:
    if user_name == st.secrets.USER and password == st.secrets.PASSWORD:
        st.success(f'Success')
        time.sleep(1)
        st.session_state.authenticated = True
        st.rerun()
    else:
      st.error('Login credentials do not match our records')
