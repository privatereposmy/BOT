import os
import logging
from logging.handlers import RotatingFileHandler


FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001749692212"))

API_HASH = os.environ.get("API_HASH", "5820bc246505e0ff60af5391d649f9a6")

APP_ID = int(os.environ.get("APP_ID", "8406611"))

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001641979770"))

OWNER_ID = int(os.environ.get("OWNER_ID", "1467649219"))

