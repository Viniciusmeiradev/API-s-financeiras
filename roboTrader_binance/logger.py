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
}
