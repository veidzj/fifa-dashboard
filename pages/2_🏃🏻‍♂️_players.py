import streamlit as st

st.set_page_config(
  page_title='FIFA DASHBOARD - Players',
  page_icon='⚽',
  layout='wide'
)

df_data = st.session_state['data']

clubs = df_data['Club'].unique()
club = st.sidebar.selectbox('Club', clubs)

df_players = df_data[(df_data['Club'] == club)]
players = df_players['Name'].unique()
player = st.sidebar.selectbox('Player', players)

player_stats = df_data[df_data['Name'] == player].iloc[0]

st.image(player_stats['Photo'])
st.title(player_stats['Name'])

st.markdown(f'**Club:** {player_stats["Club"]}')
st.markdown(f'**Position:** {player_stats["Position"]}')

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f'**Age:** {player_stats["Age"]}')
col2.markdown(f'**Height:** {player_stats["Height(cm.)"] / 100}m')
col3.markdown(f'**Weight (kg):** {player_stats["Weight(lbs.)"] * 0.453:.2f}kg')
st.divider()

st.subheader(f'Overall {player_stats["Overall"]}')
st.progress(int(player_stats['Overall']))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label='Market value', value=f'£ {player_stats["Value(£)"]}')
col2.metric(label='Weekly wage', value=f'£ {player_stats["Wage(£)"]}')
col3.metric(label='Release clause', value=f'£ {player_stats["Release Clause(£)"]}')
