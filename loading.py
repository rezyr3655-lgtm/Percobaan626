import os
import time
from config import COLOR

def loading():
    os.system("clear")

    print(COLOR["cyan"] + "\nLoading XNX Theme...\n" + COLOR["reset"])

    bar = 30

    for i in range(bar + 1):
        persen = int(i / bar * 100)
        penuh = "█" * i
        kosong = "░" * (bar - i)

        print(f"\r[{penuh}{kosong}] {persen}%", end="")
        time.sleep(0.05)

    print("\n")
