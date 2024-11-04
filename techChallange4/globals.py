import pandas as pd
import os
from dotenv import load_dotenv, dotenv_values
from prophet import Prophet
from prophet.serialize import model_to_json, model_from_json
import requests

global insights
insights = ['1998','2008','2011','2012','2014','2020','2022']

# Cria o dataframe que será usado em todo o projeto
global df
df = pd.read_csv('https://raw.githubusercontent.com/Rogeriom49/4DTAT/main/techChallange4/datasets/dados_mes_ano.csv', sep=",", parse_dates=['data'])

# Cria dataframe com a data como index
global df_index
df_index = pd.read_csv('https://raw.githubusercontent.com/Rogeriom49/4DTAT/refs/heads/main/techChallange4/datasets/dados_puros.csv', parse_dates=['data'], index_col='data')

# Cria dataframe para o prophet
global df_prophet
# with open("https://raw.githubusercontent.com/Rogeriom49/4DTAT/refs/heads/main/techChallange4/modelo_prophet.json", "r") as json_file:
#     model = model_from_json(json_file.read())

response = requests.get("https://raw.githubusercontent.com/Rogeriom49/4DTAT/refs/heads/main/techChallange4/modelo_prophet.json")
model_json = response.text

model = model_from_json(model_json)


future = model.make_future_dataframe(periods=365)
forecast = model.predict(future)
