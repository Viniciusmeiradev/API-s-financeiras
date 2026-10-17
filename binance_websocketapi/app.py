import pandas as pd;
import os;
import json;
import requests;

from binance.client import Client;
from dotenv import load_dotenv;

url = "https://api.binance.com/api/v3/ticker/price"
headers = {'content:type': 'application/json', 'X-MBX-APIKEY': api_key}

load_dotenv();
api_key = os.environ['BINANCE_API_KEY'];
api_secret = os.environ['BINANCE_API_SECRET'];

cliente = Client(api_key, api_secret, testnet=True);
ticket_ativos = cliente.get_all_tickers();
print(ticket_ativos);

lista_dinamica = pd.DataFrame(ticket_ativos);
lista_dinamica.head();

response = requests.get(url, headers=headers);
response = json.loads(response.text)
print(response);

lista_dinamica = pd.DataFrame.from_records(response);
lista_dinamica.head();

