import pandas as pd;
import os;
import json;
import requests;
import datetime;

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


#Status servidor
cliente.ping()


#tempo servidor
data_servidor = cliente.get_server_time();
print(data_servidor)
tempo_servidor = data_servidor['serverTime'] / 1000;
data_padrao = datetime.datetime.fromtimestamp(tempo_servidor);
data_padrao.strftime("%Y-%m-%d %H:%M:%S");


#Lista todas as criptos
moeda_infomacao = cliente.get_all_tickers()
lista_dinamica = pd.DataFrame(moeda_infomacao)
lista_dinamica.head()

#Marcadores
informacao_ativos = cliente.get_exchange_info();
informacao_ativos.keys();
lista_dinamica = pd.DataFrame(informacao_ativos['symbols']);
print(lista_dinamica);

informacao_ativo = cliente.get_symbol_info('BTCBUSD');
print(informacao_ativo);


#Livro de ofertas
lista_ofertas = cliente.get_order_book(symbol='BTCBUSD')
print(lista_ofertas)

ofertas = pd.DataFrame(lista_ofertas['ofertas']);
ofertas.columns = ['preco', 'ofertas'];
solicitacao = pd.DataFrame(lista_ofertas['solicitacao']);
solicitacao.columns = ['preco', 'solicitacao'];
lista_dinamica = pd.concat([ofertas, solicitacao]).fillna(0);
print(lista_dinamica);
