import streamlit as st
import streamlit.components.v1 as components

st.header('**Dashboard**')

iframe_url = "https://app.powerbi.com/view?r=eyJrIjoiYmZhZTk3ZjgtMDNkZi00NzU2LTlkYjEtZjUxZDcwODkyY2NlIiwidCI6IjZkYzg3NGNlLWRkMmItNGFhOS05ZjBkLWFkYjkyNjlhNzU4MCJ9"

components.iframe(iframe_url, width=1400, height=650)



