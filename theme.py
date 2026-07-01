# theme.py

import os

THEMES = {
    "1": {
        "name": "Cyber Blue",
        "color": "\033[96m"
    },
    "2": {
        "name": "Matrix Green",
        "color": "\033[92m"
    },
    "3": {
        "name": "Bloody Red",
        "color": "\033[91m"
    },
    "4": {
        "name": "Golden Yellow",
        "color": "\033[93m"
    },
    "5": {
        "name": "Purple Hacker",
        "color": "\033[95m"
    },
    "6": {
        "name": "Rainbow",
        "color": "\033[36m"
    }
}

RESET = "\033[0m"

def save_theme(color):
    with open(".theme", "w") as f:
        f.write(color)

def load_theme():
    try:
        with open(".theme") as f:
            color = f.read().strip()
    except:
        color = "\033[96m"

    return {
        "cyan": color,
        "green": color,
        "yellow": color,
        "reset": "\033[0m"
    }

def theme_menu():

    os.system("clear")

    print("""
=========================
      PILIH THEME
=========================

1. Cyber Blue
2. Matrix Green
3. Bloody Red
4. Golden Yellow
5. Purple Hacker
6. Rainbow

0. Kembali

=========================
""")

    pilih = input("\nTekan Enter...")
os.system("clear")

    if pilih == "0":
        return

    if pilih in THEMES:
        save_theme(THEMES[pilih]["color"])
        print(f"\nTheme berhasil diganti menjadi {THEMES[pilih]['name']}")
    else:
        print("\nTheme tidak tersedia.")
