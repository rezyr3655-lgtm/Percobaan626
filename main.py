#!/usr/bin/env python3

import os

from config import *
from loading import loading
from menu import menu
from theme import theme_menu
...
COLOR = load_theme()
...
loading()
menu()

os.system("clear")

with open("logo.txt", encoding="utf-8") as f:
    print(COLOR["cyan"] + f.read() + COLOR["reset"])

print(COLOR["yellow"] + TOOL_NAME)
print("Version :", VERSION)
print("Author  :", AUTHOR)
print(COLOR["reset"])

loading()

menu()
