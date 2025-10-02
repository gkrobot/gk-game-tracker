import streamlit as st
import pandas as pd

# Import the connection object type
from streamlit_gsheets import GSheetsConnection 

# Use the connection defined in secrets.toml under [connections.gsheets]
conn = st.connection("gsheets", type=GSheetsConnection)

# Read data from the first worksheet, using st.cache_data for caching.
# 'ttl="10m"' means the data will be cached for 10 minutes.
@st.cache_data(ttl="10m")
def load_data():
    df = conn.read(worksheet="Sheet1", usecols=list(range(4))) # Example: read first 4 columns
    # Fill NaN values with an empty string for easier handling
    df = df.fillna("")
    return df

data_df = load_data()

st.title("Data from Google Sheet")
st.dataframe(data_df)
