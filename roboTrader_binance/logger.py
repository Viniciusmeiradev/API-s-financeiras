import logging
from datetime import datetime

logging.basicConfig(
    filename = "src/logs/trading_bot.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s %(message)s"
)
