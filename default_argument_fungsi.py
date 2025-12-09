# Default argument

# def fungsi(argument):
# def fungsi(argument = nilai defaultnya)

# contoh 1
def say(nama = "ganteng"):
    print(f"Hallo {nama}")

say("Mahdi")
say()

# contoh 2
def sapa_dia(nama = "Reja", pesan = "apa kabar?"):
    print(f"Hai {nama}, {pesan}")

sapa_dia("Mahdi", "ada apa sayang??")
sapa_dia("Mahdi")

# contoh 3
def hitung_pangkat(angka = 3, pangkat = 2):
    hasil = angka ** pangkat
    return hasil

print(hitung_pangkat(pangkat = 3, angka = 2))

# contoh 4
def hitung_tambah(angka1=1, angka2=2, angka3=3, angka4=4):
    hasil = angka1 + angka2 + angka3 + angka4
    return hasil

print(hitung_tambah(angka2 = 3))