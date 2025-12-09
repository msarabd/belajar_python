# Latihan fungsi

import os

# program menghitung luas dan keliling persegi panjang

# membuat header progran
# os.system("cls")

# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-' * 40:^40}")

# # mengambil input user
# panjang = int(input("\nMasukkan nilai panjang = "))
# lebar = int(input("Masukkan nilai lebar = "))

# # program  menghitung luas & keliling
# luas = panjang * lebar
# keliling = 2 * (panjang + lebar)

# # tampilkan hasilnya
# print(f"\nLuas persegi panjang Anda adalah = {luas}")
# print(f"keliling persegi panjang Anda adalah = {keliling}")

def header():
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-' * 40:^40}")

def input_user():
    panjang = int(input("Masukkan nilai panjang = "))
    lebar = int(input("Masukkan nilai lebar = "))
    return panjang, lebar

def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    return luas

def hitung_keliling(panjang, lebar):
    keliling = 2 * (panjang + lebar)
    return keliling

def tampil(message, value):
    print(f"Hasil perhitungan {message} = {value}")
    
while True:
    os.system("cls")
    header()

    try:
        opsi = input("\nMau hitung luas(1) atau keliling(2) = ")
        print()
        panjang, lebar = input_user()
        
        if opsi == "1":
            luas = hitung_luas(panjang, lebar)
            tampil("luas", luas)

        elif opsi == "2":
            keliling = hitung_keliling(panjang, lebar)
            tampil("keliling", keliling)

    except:
        input("\n(Input tidak valid, ketuk enter untuk kembali)")
        continue

    try:
        isContinue = input("\napakah ingin lanjut (y/n) = ")
        if isContinue == "n":
            break
        elif isContinue == "y":
            continue

    except:
        input("\n(Input tidak valid, ketuk enter untuk kembali)")
        continue
    