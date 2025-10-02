import streamlit as st
import pandas as pd

# Import the connection object type
from streamlit_gsheets import GSheetsConnection

def google_connection():
    
    # 1. Initialize the connection
    conn = st.connection("gsheets", type=GSheetsConnection)
    
    # --- Data Loading Function with Caching ---
    
    @st.cache_data(ttl="10m", show_spinner=False)
    def load_data():
        st.write("🔄 Loading data from Google Sheets...")
        # conn.read() is the function that actually hits the Sheets API
        df = conn.read(worksheet="Sheet1", usecols=list(range(4))) 
        df = df.fillna("")
        st.write("✅ Data loaded!")
        return df

    # --- App Layout and Logic ---

    st.title("Data from Google Sheet")

    # The Refresh Button
    if st.button('🔄 Refresh Data Manually'):
        # 2. CLEAR THE GSheetsConnection CACHE
        # This clears the internal cache of the gsheets connection object.
        conn.clear()
        
        # 3. CLEAR THE st.cache_data CACHE
        # This forces the load_data function to re-run and get a new result.
        load_data.clear()
        
        st.success("Data cache cleared and fresh data requested!")
        
        # We need to rerun the app to apply the cache clear and re-load the data
        # Note: st.rerun() is available in Streamlit version 1.28.0 and higher.
        st.rerun()
        
    # Load and display the data
    # This will now fetch new data because the cache was cleared (steps 2 & 3).
    data_df = load_data()
    
    # Display the DataFrame
    st.dataframe(data_df)

# google_connection()