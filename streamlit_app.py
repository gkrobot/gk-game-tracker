import streamlit as st
import time

from functions.authentication import Authenticator

st.title("Welcome to gameTrax")

if 'authenticated' not in st.session_state or st.session_state.authenticated == False:
    st.write('Not authenticated')
    st.session_state.authenticated = False
    authenticator = Authenticator()

# if 'authenticated' not in st.session_state:
#   st.session_state.authenticated = False

# if st.session_state.authenticated == True:
  
#   game_options = [None, "Phase 10", "Skip-Bo", "Uno"]
  
#   selected_game = st.selectbox(label="Select your game", options=game_options, index=0)
  
#   if selected_game:
#     st.info(f"You're playing {selected_game}!")
  
#   if st.button('Log out'):
#     st.session_state.authenticated = False
#     st.rerun()

# else:
#   st.session_state.user_name = st.text_input(label="Enter username", autocomplete="username")
#   st.session_state.password = st.text_input(label="Enter password", type="password", autocomplete="current-password")
  
#   if st.session_state.user_name and st.session_state.password:
#     if st.session_state.user_name == st.secrets.USER and st.session_state.password == st.secrets.PASSWORD:
#         st.success(f'Success')
#         time.sleep(1)
#         st.session_state.authenticated = True
#         st.session_state.password = None
#         st.rerun()
#     else:
#       st.error('Login credentials do not match our records')
