import streamlit as st
import streamlit.components.v1 as components

st.header('**Dashboard**')

iframe_url = "https://app.powerbi.com/reportEmbed?reportId=61457650-2823-4dce-a1b7-10faa41edbc7&autoAuth=true&ctid=6dc874ce-dd2b-4aa9-9f0d-adb9269a7580"

components.iframe(iframe_url, width=1400, height=650)



