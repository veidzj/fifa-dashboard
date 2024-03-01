import streamlit as st

df_data = st.session_state['data']

clubs = df_data['Club'].unique()
club = st.sidebar.selectbox('Club', clubs)

df_players = df_data[(df_data['Club'] == club)]
players = df_players['Name'].unique()
player = st.sidebar.selectbox('Player', players)
