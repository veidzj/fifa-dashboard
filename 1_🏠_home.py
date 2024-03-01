import streamlit as st
import webbrowser

st.markdown('# FIFA DASHBOARD')
st.sidebar.markdown('Developed by [veidzj](https://github.com/veidzj)')

btn = st.button('Access the data on Kaggle')
if btn:
  webbrowser.open_new_tab('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

st.markdown('The Football Player Dataset from 2017 to 2023 provides comprehensive information about professional football players. The dataset contains a wide range of attributes, including player demographics, physical characteristics, playing statistics, contract details, and club affiliations. \n\n With **over 17,000 records**, this dataset offers a valuable resource for football analysts, researchers, and enthusiasts interested in exploring various aspects of the footballing world, as it allows for studying player attributes, performance metrics, market valuation, club analysis, player positioning, and player development over time.')
