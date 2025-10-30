import streamlit as st
import time

from functions.authentication import Authenticator
authenticator = Authenticator()

from functions.google_connection import google_connection

st.title("Welcome to gameTrax")

# Authenticate using username and password
col1, col2 = st.columns(2)

with col1:
    if 'authenticated' not in st.session_state or st.session_state.authenticated == False:
        st.session_state.authenticated = False
        authenticator.login()

if 'authenticated' in st.session_state and st.session_state.authenticated == True:
    google_connection()
    if st.button('Logout'):
        authenticator.logout()

