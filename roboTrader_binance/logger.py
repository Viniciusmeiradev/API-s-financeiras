import logging
from datetime import datetime

logging.basicConfig(
    filename = "src/logs/trading_bot.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s %(message)s"
)

def CriaOrdemLog(order){
    lado = order["side"]
    tipo = order["type"]
    quantidade = order["executedQty"]
    ativo = order["symbol"]
    PrecoUnidade = order["fills"][0]["price"]
    moeda = order["fills"][0]["commisionAsset"]
    valorTotal = order["cummulativeQuoteQty"]
    tempo = order["transactTime"]
    data = datetime.utcfromtimestamp(tempo / 1000).strftime("(%H:%M:%S) %Y-%m-%d")
}
