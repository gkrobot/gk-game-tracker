import streamlit as st
import pandas as pd

# Import the connection object type
from streamlit_gsheets import GSheetsConnection

# 1. Define the connection outside the main function/loop
# This makes it easier to access in the callback
conn = st.connection("gsheets", type=GSheetsConnection)

# --- Data Loading Function with Caching ---

@st.cache_data(ttl="10m", show_spinner=False)
def load_data():
    st.info("🔄 Loading data from Google Sheets...")
    # conn.read() is the function that actually hits the Sheets API
    df = conn.read(worksheet="Sheet1", usecols=list(range(4))) 
    df = df.fillna("")
    st.success("✅ Data loaded!")
    return df

# --- Callback Function to Clear Caches ---

def clear_caches():
    """Clears both the GSheets connection cache and the st.cache_data cache."""
    st.info("Clearing caches...")
    # Clear the internal cache of the gsheets connection object.
    conn.clear()
    
    # Force the st.cache_data function to re-run.
    load_data.clear()
    
    # Set a state variable to confirm refresh was triggered (optional)
    st.session_state['data_refreshed'] = True

def google_connection():
    
    st.title("Data from Google Sheet")
    
    # 2. Attach the clear_caches function to the button using 'on_click'
    st.button(
        '🔄 Refresh Data Manually', 
        on_click=clear_caches
    )
    
    # Optional: Display a message after a successful manual refresh
    if st.session_state.get('data_refreshed'):
        st.success("Data refresh triggered. Loading new data now...")
        # Reset the state so the message only appears once
        st.session_state['data_refreshed'] = False

    # 3. Load and display the data
    data_df = load_data()
    
    # 4. Display the DataFrame
    st.dataframe(data_df)

# Call the main function
# google_connection()