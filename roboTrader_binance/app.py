import os
import time
from datetime import datetime
import logging
import pandas as pd

from binance.client import Client
from binance.enums import *
from logger import *

api_key = os.getenv("BINANCE_API_KEY")
secret_key = os.getenv("BINANCE_SECRET_KEY")

codigoMoeda = "BTC"
codigoOperacao = "BTCBRL"
candlePeriodo = Client.KLINE_INTERVAL_15MINUTE
quantidadeTrade = 0.01

Class BinanceTraderBot():
    ultima_descisao_trade : bool #False = Vender/True = Comprar

    def __init__(self, codigoCripto, codigoNegociado, quantidadeTrader, porcentagemNegociada, periodoVela):
        self.codigoCripto = codigoCripto
        self.codigoNegociado = codigoNegociado
        self.quantidadeTrader = quantidadeTrader
        self.porcentagemNegociada = porcentagemNegociada
        self.periodoVela = periodoVela;

        self.clienteBinance = Client(api_key, secret_key)
        self.atualizarDados()
        print("--------------------------------------------")
        print("Robo Trader Iniciado...")


    def atualizarDados(self):
        self.

jfsjajja
