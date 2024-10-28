import pandas as pd
import streamlit as st
import globals
import matplotlib.pyplot as plt
import plotly.express as px
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

# st.set_page_config(layout='wide', 
#                    page_title='EDA')

st.header('**EDA**')

t1, t2, t3  = st.tabs(['Estatisticas', 'Análise de Série Temporal', 'Análise de Dados Estacionários'])

with t1:
    st.subheader('Estatisticas Descritiva')
    col3, col4, col5 = st.columns(3)
    with col3:
        st.metric(label="Média Preço", value=f'US${globals.df_index.preco.mean().round(2)}')
    with col4:
        st.metric(label="Mediana Preço", value=globals.df_index.preco.median())
    with col5:
        st.metric(label="Desvio Padrão Preço", value=globals.df_index.preco.std().round(2))

    col6, col7, col8 = st.columns(3)
    with col6:
        st.metric(label="Mínimo Preço", value=f'US${globals.df.preco.min()}')
        st.metric(label="Data do Valor Mínimo", value=globals.df['data'].iloc[8329].strftime('%d/%m/%Y'))
    with col7:
        st.metric(label="Máximo Preço", value=f'US${globals.df.preco.max()}')
        st.metric(label="Data do Valor Máximo", value=globals.df['data'].iloc[5221].strftime('%d/%m/%Y') )
    with col8:
        st.metric(label="Variância", value=globals.df_index.preco.var().round(2))
    
with t2:
    col1, col2 = st.columns(2)
    resultados = seasonal_decompose(globals.df_index, period=375)
    with col1:
        st.subheader('Sazonalidade')
        fig = px.line(resultados.seasonal, x=resultados.seasonal.index, y=resultados.seasonal.values.round(2), labels={'x':'Anos', 'y':'Preço'})
        st.plotly_chart(fig)

    with col2:
        st.subheader('Tendência')
        fig2 = px.line(resultados.trend, x=resultados.trend.index, y=resultados.trend.values.round(2), labels={'x':'Anos', 'y':'Preço'})
        st.plotly_chart(fig2)

with t3:
    st.subheader('Análise de Dados Estacionários')
    x = globals.df_index.preco.values
    result = adfuller(x)
    st.write(f'p-Valor',  format(result[1]*100,'.2f'))
    st.write(f'**p-valor superior a 5% indicando dado não estacionário**')
