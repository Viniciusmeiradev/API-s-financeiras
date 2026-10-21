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


#trades recentes
trades_recentes = cliente.get_recent_trades(symbol='BTCBUSD')
lista_dinamica = pd.DataFrame(trades_recentes)
lista_dinamica.head()


#historico trades
id = lista_dinamica.loc[450,'id']
historico_trades = cliente.get_historical_trades(symbol='BTCBUSD', limit=1000, fromId=id)
lista_dinamica = pd.DataFrame(historico_trades)
print(lista_dinamica)


#preco medio
preco_medio = cliente.get_avg_price(symbol='BTCBUSD')
print(preco_medio)


#preco de todas as criptos
ticket = cliente.get_ticker()
lista_dinamica = pd.DataFrame(ticket)
print(lista_dinamica)


#informacao de conta
informacao_conta = cliente.get_account()
print(informacao_conta)


#detalhes de ativos
detalhes_ativos = cliente.get_asset_balance(asset='ETH')
print(detalhes_ativos)


#Historico de negociaçao
negociacoes_executadas = cliente.get_my_trades(symbol='BTCBUSD')
print(negociacoes_executadas)


#Todas as ordens
buscar_ordens = cliente.get_all_orders(symbol = 'BTCBUSD')
print(buscar_ordens)


#Teste orden de compra
ordem_compra = cliente.create_test_order(symbol='BTCBUSD', side='BUY', type='MARKET', quantity=0.0005)
print(ordem_compra)


#Solicitacao de compra real
solicitar_compra = cliente.order_market_buy(symbol='BTCBUSD', quantity=0.005)
print(solicitar_compra)


#Status da ordem
status_ordem = cliente.get_order(symbol='BTCBUSD', orderId=status_ordem['orderId'])
print(status_ordem)


#Cancelar ordem
cancelar_ordem = cliente.cancel_order(symbol='BTCBUSD', orderId='your_order_id')


#Socket Url
symbol = 'btcusdt'
socket = f'wss://stream.binance.com:9443/ws/{symbol}@trade'


#Trade Socket
def on_mensagem(ws, message):
    converter = json.loads(message)
    lista_conversao = [(converter['T'], converter['P'])]
    global lista_dinamica
    lista_dinamica = pd.concat([lista_dinamica, pd.DataFrame.from_records(lista_conversao)])

def on_error(ws, error):
    print(error)

def on_fechado(ws, close_status_code, close_msg):
    print("Fechado")
    lista_dinamica.columns = ['time', 'price']
    lista_dinamica['time'] = pd.to_datetime(df['time'], unit='ms')
    lista_dinamica.set_index(lista_dinamica['time'], inplace=True)
    lista_dinamica.drop(columns='time', inplace=True)
    print(lista_dinamica)

def on_aberto(ws):
    print("Opened connection")

ws = websocket.WebSocketApp(socket,
                            on_aberto = on_aberto, 
                            on_mensagem = on_mensagem,
                            on_error = on_error,
                            on_fechado = on_fechado)

ws.run_forever()
