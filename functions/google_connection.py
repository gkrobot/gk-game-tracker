import streamlit as st
import pandas as pd

# Import the connection object type
from streamlit_gsheets import GSheetsConnection

def google_connection():
    
    # Use the connection defined in secrets.toml under [connections.gsheets]
    conn = st.connection("gsheets", type=GSheetsConnection)
    
    # --- Data Loading Function with Caching ---
    
    # Read data from the first worksheet, using st.cache_data for caching.
    'ttl="10m"' means the data will be cached for 10 minutes.
    # The 'show_spinner=False' is added to avoid a duplicate spinner when the 
    # button is pressed and the function is re-run.
    @st.cache_data(ttl="10m", show_spinner=False)
    def load_data():
        st.write("🔄 Loading data from Google Sheets...") # Optional: show a loading message
        df = conn.read(worksheet="Sheet1", usecols=list(range(4))) # Example: read first 4 columns
        # Fill NaN values with an empty string for easier handling
        df = df.fillna("")
        st.write("✅ Data loaded!") # Optional: show success message
        return df

    # --- App Layout and Logic ---

    st.title("Data from Google Sheet")

    # 1. Add the Refresh Button
    # When the button is clicked, it returns True.
    if st.button('🔄 Refresh Data Manually'):
        # 2. Clear the cache for the specific function.
        # This forces Streamlit to re-run the `load_data` function and fetch new data.
        load_data.clear()
        # Optional: Display a confirmation message
        st.success("Data refresh triggered!")
        
    # 3. Load and display the data
    # This will use the cached data if available, or fetch new data if the cache was cleared.
    data_df = load_data()
    
    # 4. Display the DataFrame
    st.dataframe(data_df)

