#!/usr/bin/env python3

import os
import time
from config import *

os.system("clear")

# Membaca logo
with open("logo.txt", "r", encoding="utf-8") as f:
    logo = f.read()

print(COLOR["cyan"] + logo + COLOR["reset"])

print(COLOR["green"] + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f" Tool    : {TOOL_NAME}")
print(f" Version : {VERSION}")
print(f" Author  : {AUTHOR}")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" + COLOR["reset"])

print()

print(COLOR["yellow"] + "Loading..." + COLOR["reset"])

for i in range(101):
    print(f"\r[{i}%]", end="")
    time.sleep(0.02)

print("\n")

print(COLOR["cyan"] + "[1] Start")
print("[2] About")
print("[0] Exit" + COLOR["reset"])

menu = input("\nPilih : ")

if menu == "1":
    print("Tool akan dijalankan...")
elif menu == "2":
    print("XNX Theme by xnx jakarta")
else:
    print("Bye...")
