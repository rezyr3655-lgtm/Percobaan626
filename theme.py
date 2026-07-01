from config import COLOR

THEMES = {
    "1": {
        "nama": "Default",
        "warna": COLOR["cyan"]
    },
    "2": {
        "nama": "Merah",
        "warna": COLOR["red"]
    },
    "3": {
        "nama": "Hijau",
        "warna": COLOR["green"]
    },
    "4": {
        "nama": "Kuning",
        "warna": COLOR["yellow"]
    },
    "5": {
        "nama": "Biru",
        "warna": COLOR["blue"]
    }
}

theme = THEMES["1"]

def pilih_theme():
    global theme

    print("""
====== PILIH THEME ======

1. Default
2. Merah
3. Hijau
4. Kuning
5. Biru

=========================
""")

    pilih = input("Pilih Theme : ")

    if pilih in THEMES:
        theme = THEMES[pilih]
        print("Theme berhasil diganti ke", theme["nama"])
    else:
        print("Theme tidak tersedia.")
