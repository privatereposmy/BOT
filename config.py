import os
import logging
from logging.handlers import RotatingFileHandler


FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001749692212"))
