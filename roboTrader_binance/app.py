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



class BinanceTraderBot:

    ultima_descisao_trade: bool = False;  #False = Vender/True = Comprar

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



    def getAtualizarDadosConta(self):
        return self.clienteBinance.get_account()


    def getBalancoAtualCarteira(self):
        carteira = 0.0

        for cripto in self.dados_conta['balances']:
            if cripto['asset'] == self.codigoCripto:
                carteira = cripto['free']
        
        return float(carteira)

            
    def getPosicaoAtual(self): 
        if self.balancoAtualCarteira > 0.001:
            return True #Comprado
        else:
            return False #Vendido


    def getDadosAcaoAtual(self):
        velas = self.clienteBinance.get_klines(symbol = self.codigoNegociado, interval = self.periodoVela, limit = 500)
        precos = pd.DataFrame(velas)
        precos.columns = ["open_time", "open_price", "high_price", "low_price", "close_price", "volume", "close_time", 
                          "quote_asset_volume","number_of_trades", "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "-"]
        
        precos = precos[["close_price", "open_time"]]
        precos["open_time"] = precos["open_time"].dt.tz_convert("America/Sao_Paulo")
        precos["open_time"] = pd.to_datetime(precos["open_time"], unit="ms").dt.tz_localize("UTC")
        return precos




    def atualizarDados(self):
        self.dados_conta = self.getAtualizarDadosConta()
        self.balancoAtualCarteira = self.getBalancoAtualCarteira()
        self.posicaoAtual = self.getPosicaoAtual()
        self.dadosAcao = self.getDadosAcaoAtual()



bot = BinanceTraderBot(
    codigoCripto=codigoMoeda,
    codigoNegociado=codigoOperacao,
    quantidadeTrader=quantidadeTrade,
    porcentagemNegociada=10,
    periodoVela=candlePeriodo
)





def getEstrategiaMediaMovel(self, fast_window=7, slow_window=40):
        # Calculo das medias moveis
        self.dadosAcao["ma_fast"] = self.dadosAcao["close_price"].rolling(window=fast_window).mean()
        self.dadosAcao["ma_slow"] = self.dadosAcao["close_price"].rolling(window=slow_window).mean()

        # Ultimas medias
        ultimaMediaRapida = self.dadosAcao["ma_fast"].iloc[-1]
        ultimaMediaLenta = self.dadosAcao["ma_slow"].iloc[-1]

        if ultimaMediaRapida > ultimaMediaLenta:
            ma_trade_decision = True  # Compra
        else:
            ma_trade_decision = False  # Vende

        print("**********************************")
        print("Estrategia Executada com Sucesso.")
        print(f"({self.codigoNegociado})")
        print(f"{ultimaMediaRapida:.3f} - Media Rapida")
        print(f"{ultimaMediaLenta:.3f} - Media Lenta")
        print(f"Decisao de posicao: {'Comprar' if ma_trade_decision else 'Vender'}")
        print("**********************************")

        return ma_trade_decision




def getCalculoVolatilidade(self, fast_window = 7, slow_window = 40):
    # Calculo medias moveis
    self.dadosAcao["ma_fast"] = self.dadosAcao["close_price"].rolling(window=fast_window).mean()
    self.dadosAcao["ma_slow"] = self.dadosAcao["close_price"].rolling(window=slow_window).mean()

    #Calculo volatilidade
    self.dadosAcao["volatility"] = self.dadosAcao["close_price"].rolling(window=slow_window).std()

    #Calculo Gradiente
    ultimaMediaRapida = self.dadosAcao["ma_fast"].iloc[-1]
    penultimaMediaRapida = self.dadosAcao["ma_fast"].iloc[-3]

    ultimaMediaLenta = self.dadosAcao["ma_slow"].iloc[-1]
    penultimaMediaLenta = self.dadosAcao["ma_slow"].iloc[-3]



