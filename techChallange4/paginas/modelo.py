import pandas as pd
import streamlit as st
import globals
from datetime import timedelta
import graficos

st.header('**Modelo**')

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input(label='Data Inicial', 
                                                                  format='DD-MM-YYYY', 
                                                                  min_value=globals.df['data'].dt.date.max(), 
                                                                  value=globals.df['data'].dt.date.max(), 
                                                                  max_value=globals.forecast['ds'].dt.date.max())

with col2:
    end_date = st.date_input(label='Data Final', 
                                                                format='DD-MM-YYYY', 
                                                                min_value=globals.df['data'].dt.date.max(), 
                                                                value=globals.df['data'].dt.date.max() + timedelta(days=30), 
                                                                max_value=globals.forecast['ds'].dt.date.max())

mask = (globals.forecast['ds'].dt.date >= start_date) & (globals.forecast['ds'].dt.date <= end_date)

st.plotly_chart(graficos.lineChart(dataframe=globals.forecast.loc[mask], 
                                   x='ds', 
                                   y=['yhat_upper','yhat','yhat_lower'], 
                                   title='Previsão', 
                                   xaxis_title='Data', 
                                   yaxis_title='Previsão',
                                   legendas={'yhat_upper':'Intervalo Superior', 
                                             'yhat':'Previsão', 
                                             'yhat_lower':'Intervalo Inferior'}), 
                use_container_width=True)

with st.expander('**Considerações**'):
    st.write(""" O gráfico apresentado anteriormente remete aos resultados do modelo Prophet, onde os preços do petróleo foram previsões com base nos dados disponibilizados. """)
    st.write(""" Para ver o notebook do modelo [clique aqui](https://github.com/Rogeriom49/4DTAT/blob/main/techChallange4/notebooks/modelo.ipynb). """ )