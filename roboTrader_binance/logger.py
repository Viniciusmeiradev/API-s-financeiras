import logging
from datetime import datetime

logging.basicConfig(
    filename = "src/logs/trading_bot.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s %(message)s"
)

def CriaOrdemLog(order):
    lado = order["side"]
    tipo = order["type"]
    quantidade = order["executedQty"]
    ativo = order["symbol"]
    PrecoUnidade = order["fills"][0]["price"]
    moeda = order["fills"][0]["commisionAsset"]
    valorTotal = order["cummulativeQuoteQty"]
    tempo = order["transactTime"]
    data = datetime.utcfromtimestamp(tempo / 1000).strftime("(%H:%M:%S) %Y-%m-%d")

    logMessage = (
        "\n------------------------\n"
        "ORDEM EXECUTADA:\n"
        f"Lateralização: {lado}\n"
        f"Tipo: {tipo}\n"
        f"Ativo: {ativo}\n"
        f"Quantidade: {quantidade}\n"
        f"Valor no momento: {PrecoUnidade}\n"
        f"Moeda: {moeda}\n"
        f"Valor {moeda}: {valorTotal}z\n"
        f"Data/Hora: {data}\n"
        "\n"
        "Ordem Completa: \n"
        f"{order}"
        "\n------------------------\n"
    )

    printMessage = (
        "\n------------------------\n"
        "ORDEM EXECUTADA:\n"
        f"Lateralização: {lado}\n"
        f"Tipo: {tipo}\n"
        f"Ativo: {ativo}\n"
        f"Quantidade: {quantidade}\n"
        f"Valor no momento: {PrecoUnidade}\n"
        f"Moeda: {moeda}\n"
        f"Valor {moeda}: {valorTotal}z\n"
        f"Data/Hora: {data}\n"
        "\n"
        "Ordem Completa: \n"
        f"{order}"
        "\n------------------------\n"
    )
    print(printMessage)
    logging.info(logMessage)

if __name__ == "__main__":
    ordemVenda = {
        'symbol' : 'BTCBRL',
        'ordemId': 180636560,
        'ordemListaId' : -1,
        'clienteOrdemId' : 'x-asdasd',
        'tempoTransacao' : 1733438637687,
        'preco': 0.000000,
        'origemQty' : 0.19900000,
        'qtyExecutada' : 0.19900000,
        'qtyAcumulada' : '279.2169000',
        'status' : 'FILLED',
        'tempoForca' : 'GTC',
        'tipo': 'MARKET',
        'lado':'SELL',
        'tempoTrabalhado' : 1733438637638,
        'filtros': [
            {
                'preco' : '1403.100000',
                'quantidade':'0.1990000',
                'comissao' : '0.27921690',
                'comissaoAtivo' : 'BRL',
                'tradeId':'4293074'
            }
        ],
        'modoPrevencaoTrade' :' EXPIRE_MARKET'
    }
    CriaOrdemLog(ordemVenda)
