import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

STAT_STICK = os.environ.get("STAT_STICK", "CAACAgUAAxkBAAIMMmJ_Y17NRUpBJgLhsqUTTRNilYxAAAKeBAACf7TwVxZUQiDRe7p1HgQ")

PICS = os.environ.get("PICS", "https://telegra.ph/file/34fd203eb89fd747ffb57.jpg").split()

DELAY = int(os.environ.get("DELAY", "2"))
