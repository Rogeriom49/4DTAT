import pandas as pd
import os
from dotenv import load_dotenv, dotenv_values
from prophet import Prophet
from prophet.serialize import model_to_json, model_from_json

load_dotenv()

# Cria o dataframe que será usado em todo o projeto
global df
df = pd.read_csv(os.getenv("DATAFRAME"), sep=",", parse_dates=['data'])

# Cria dataframe com a data como index
global df_index
df_index = pd.read_csv(os.getenv("DATAFRAME_DATA_INDEX"), parse_dates=['data'], index_col='data')

# Cria dataframe para o prophet
global df_prophet
with open("modelo_prophet.json", "r") as json_file:
    model = model_from_json(json_file.read())

future = model.make_future_dataframe(periods=365)
forecast = model.predict(future)