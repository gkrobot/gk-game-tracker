import streamlit as st
import time

from functions.authentication import Authenticator
authenticator = Authenticator()

from functions.google_connection import google_connection

st.title("welcome to gameTrax")

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

    st.session_state.selected_view = st.pills("Select View", ["Game History", "Add New Game"])
    if st.session_state.selected_view == "Game History":
        st.header("Game History")
        if 'data' in st.session_state:
            st.session_state.displayed_data = st.session_state.data #[['record_id', 'game', 'winner', 'game_time']]
            st.dataframe(st.session_state.displayed_data)
        else:
            st.write("No data available.")
    elif st.session_state.selected_view == "Add New Game":
        st.header("Add New Game")
        with st.form("add_game_form"):
            game = st.text_input("Game Name")
            winner = st.text_input("Winner")
            game_time = st.text_input("Game Time (e.g., 2024-06-01 15:30)")
            submitted = st.form_submit_button("Submit")
            if submitted:
                new_record = {
                    "game": game,
                    "winner": winner,
                    "game_time": game_time
                }
                st.session_state.google_conn.insert(new_record, worksheet="Active")
                st.success("New game record added successfully!")
                time.sleep(1)
                st.rerun()