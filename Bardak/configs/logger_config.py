from loguru import logger
import os
import sys

LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs'))
os.makedirs(LOG_DIR, exist_ok=True)

logger.configure(
    handlers=[
        {
            "sink": os.path.join(LOG_DIR, "info.log"),
            "level": "INFO",
            "rotation": "10 MB",
            "enqueue": True,
            "backtrace": True,
            "diagnose": True
        },
        {
            "sink": os.path.join(LOG_DIR, "error.log"),
            "level": "ERROR",
            "rotation": "5 MB",
            "enqueue": True,
            "backtrace": True,
            "diagnose": True
        },
        {
            "sink": sys.stderr,
            "level": "DEBUG",
            "colorize": True
        }
    ]
)
