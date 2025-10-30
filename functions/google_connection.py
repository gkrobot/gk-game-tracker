import streamlit as st
import pandas as pd

# Import the connection object type
from streamlit_gsheets import GSheetsConnection

def google_connection():
    # Create a connection object.

    conn = st.connection("gsheets", type=GSheetsConnection)
    
    st.session_state.data = conn.read(
        worksheet="Active"
    )

    st.dataframe(st.session_state.data)