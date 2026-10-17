import pandas as pd;
import os;

from binance.client import Client;
from dotenv import load_dotenv;

load_dotenv();

api_key = os.environ['BINANCE_API_KEY'];
api_secret = os.environ['BINANCE_API_SECRET'];

cliente = Client(api_key, api_secret, testnet=True);
ticket_ativos = cliente.get_all_tickers();

print(ticket_ativos);
