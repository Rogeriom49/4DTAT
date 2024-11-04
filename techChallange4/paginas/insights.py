import streamlit as st
import globals

st.header('**Insights**')


tab1, tab2,tab3,tab4, tab5, tab6, tab7 = st.tabs(globals.insights)

with tab1:
    st.subheader('Ano 1998')
    st.dataframe(globals.df_index.loc['1998'])

with tab2:
    st.subheader('Ano 2008')
    st.dataframe(globals.df_index.loc['2008'])

with tab3:
    st.subheader('Ano 2011')
    st.dataframe(globals.df_index.loc['2011'])

with tab4:
    st.subheader('Ano 2012')
    st.dataframe(globals.df_index.loc['2012'])

with tab5:
    st.subheader('Ano 2014')
    st.dataframe(globals.df_index.loc['2014'])    

with tab6:
    st.subheader('Ano 2020')    
    st.dataframe(globals.df_index.loc['2020'])    

with tab7:
    st.subheader('Ano 2022')
    st.dataframe(globals.df_index.loc['2022'])