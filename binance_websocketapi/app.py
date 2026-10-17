import pandas as pd;
import os;
import json;
import requests;

from binance.client import Client;
from dotenv import load_dotenv;

#Exemplo simples
load_dotenv();

api_key = os.environ['BINANCE_API_KEY'];
api_secret = os.environ['BINANCE_API_SECRET'];
cliente = Client(api_key, api_secret, testnet=True);
ticket_criptomoedas = cliente.get_all_tickers();
print(ticket_criptomoedas);

lista_dinamica = pd.DataFrame(ticket_criptomoedas);
lista_dinamica.head();



#Exemplo Requests
url = "https://api.binance.com/api/v3/ticker/price"
headers = {'content:type': 'application/json', 'X-MBX-APIKEY': api_key}
response = requests.get(url, headers=headers);
response = json.loads(response.text)
print(response);

lista_dinamica = pd.DataFrame.from_records(response);
lista_dinamica.head();


#EndPoints
cliente.ping()

lista_dinamica = pd.DataFrame.from_records(response);
lista_dinamica.head();

