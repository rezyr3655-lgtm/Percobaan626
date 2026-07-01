import os
from config import *
from theme import theme_menu

def menu():

    while True:

        print(COLOR["green"] + """
═══════════════════════════
         MENU
═══════════════════════════
[1] Informasi
[2] Bersihkan Layar
[3] Ganti Theme
[4] Reload
[0] Keluar
═══════════════════════════
""" + COLOR["reset"])

        pilih = input("Pilih : ")

        if pilih == "1":
    print("\nNama Tool :", TOOL_NAME)
    print("Versi     :", VERSION)
    print("Author    :", AUTHOR)
    input("\nEnter...")
    os.system("clear")

elif pilih == "2":
    os.system("clear")

elif pilih == "3":
    theme_menu()

elif pilih == "4":
    os.system("clear")

elif pilih == "0":
    print("Terima kasih.")
    break

else:
    print("Pilihan salah.")
