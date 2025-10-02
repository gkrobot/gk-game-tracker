import streamlit as st
import time

class Authenticator:
    def __init__(self):
        self.authenticated = False

    def login(self):
        user_name = st.text_input(label="Enter username", autocomplete="username")
        password = st.text_input(label="Enter password", type="password", autocomplete="current-password")
        if st.button('Login'):
            st.session_state.user_name = user_name
            st.session_state.password = password
            if user_name == st.secrets.USER and password == st.secrets.PASSWORD:
                st.success(f'Success')
                time.sleep(1)
                self.authenticated = True
                st.session_state.authenticated = True
                st.session_state.password = None
                st.rerun()
            else:
                st.error('Login credentials do not match our records')

    def logout(self):
        self.authenticated = False
        st.session_state.authenticated = False
        st.rerun()
