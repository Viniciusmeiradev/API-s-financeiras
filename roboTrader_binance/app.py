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
