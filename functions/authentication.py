import streamlit as st
import time

class Authenticator:
    def __init__(self):
        # Initialize session state variables if they don't exist
        if 'authenticated' not in st.session_state:
            st.session_state.authenticated = False
        self.authenticated = st.session_state.authenticated

    def login(self):
        # Start the form
        with st.form("login_form"):
            st.header("Login")
            
            # Input fields inside the form
            user_name = st.text_input(label="Enter username", autocomplete="username", key="form_username")
            password = st.text_input(label="Enter password", type="password", autocomplete="current-password", key="form_password")
            
            # Submit button inside the form
            submitted = st.form_submit_button('Login')
        
        # Logic executes ONLY when the form is submitted
        if submitted:
            # Assuming st.secrets.USER and st.secrets.PASSWORD are set in your environment
            try:
                # Store credentials in session state for potential debug/next run
                st.session_state.user_name = user_name
                st.session_state.password = password # This is okay for immediate validation, but will be cleared after success

                # Replace with your actual credentials check using st.secrets
                if user_name == st.secrets.USER and password == st.secrets.PASSWORD:
                    st.success(f'Login successful')
                    time.sleep(1) # Short delay for success message visibility
                    
                    # Update authentication states
                    self.authenticated = True
                    st.session_state.authenticated = True
                    st.session_state.password = None # Clear password from session state for security
                    st.rerun() # Rerun to update the app state
                else:
                    st.error('Login credentials do not match our records')
            except AttributeError:
                st.error("Configuration Error: Please ensure st.secrets.USER and st.secrets.PASSWORD are set.")
                
    def logout(self):
        self.authenticated = False
        st.session_state.authenticated = False
        st.rerun()
