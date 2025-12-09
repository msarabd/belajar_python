# Fungsi dengan argument

'''
def nama_fungsi(argument):
    Badan fungsi
'''

def hello_world(nama):
    print("Selamat datang", nama)

hello_world("vio")

# program tambah

def tambah(angka_1, angka_2):
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,5)
tambah(10000, 1)

def say_hi(data_peserta):
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")

anggota_osis = ["Ucup", "Otong", "Surotong"]

say_hi(anggota_osis)