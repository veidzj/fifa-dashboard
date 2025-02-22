import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

st.set_page_config(
  page_title='FIFA DASHBOARD',
  page_icon='⚽',
  layout='wide'
)

if 'data' not in st.session_state:
  df_data = pd.read_csv('datasets/FIFA23_official_data.csv', index_col=0)
  df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
  df_data = df_data.sort_values(by='Overall', ascending=False)
  st.session_state['data'] = df_data

st.markdown('# FIFA DASHBOARD')
st.sidebar.markdown('Developed by [veidzj](https://github.com/veidzj)')

btn = st.button('Access the data on Kaggle')
if btn:
  webbrowser.open_new_tab('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

st.markdown('The Football Player Dataset from 2017 to 2023 provides comprehensive information about professional football players. The dataset contains a wide range of attributes, including player demographics, physical characteristics, playing statistics, contract details, and club affiliations. \n\n With **over 17,000 records**, this dataset offers a valuable resource for football analysts, researchers, and enthusiasts interested in exploring various aspects of the footballing world, as it allows for studying player attributes, performance metrics, market valuation, club analysis, player positioning, and player development over time.')
