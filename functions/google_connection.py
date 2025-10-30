import streamlit as st
import pandas as pd

# Import the connection object type
from streamlit_gsheets import GSheetsConnection

def google_connection():
    # Create a connection object.

    st.session_state.google_conn = st.connection("gsheets", type=GSheetsConnection)
    
    st.session_state.data = st.session_state.google_conn.read(
        worksheet="Active"
    )
