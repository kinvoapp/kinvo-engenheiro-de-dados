import sys

from loguru import logger


def format_record() -> str:
    period = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>"
    level = "<yellow><level>{level: <8}</level></yellow>"
    local = "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"
    message = "<level>{message}</level>"

    info = " <red>|</red> ".join([period, level, local])

    return " ".join([info, ">>    ", message])


# set format
logger.configure(
    handlers=[{"sink": sys.stdout, "level": "INFO",
               "format": format_record()}]
)
