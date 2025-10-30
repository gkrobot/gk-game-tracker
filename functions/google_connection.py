import streamlit as st
import pandas as pd

# Import the connection object type
from streamlit_gsheets import GSheetsConnection

def google_connection():
    # Create a connection object.

    conn = st.connection("gsheets", type=GSheetsConnection)
    
    df = conn.read()

    # Print results.
    for row in df.itertuples():
        st.write(f"{row.name} has a :{row.pet}:")