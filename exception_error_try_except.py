import os
# exception akan terjadi saat program
# mengalami error saat runtime

# contoh penggunaan sederhana

# input_user = int(input("Masukkan angka = "))
# hasil = None

# try:
#     hasil = 10/input_user
# except:
#     print("input tidak boleh 0")

# print(f"hasil = {hasil}")

# contoh di aplikasi

while True:
    os.system("cls")
    try:
        angka = int(input("Masukkan angka = "))
        hasil = 10 / angka
        print(f'hasil = {angka}')
        isDone = input("Ingin lanjut (y/n) = ")
        if isDone == "n":
            break
        elif isDone == "y":
            continue
        

    except ValueError:
        input("\n(Input tidak valid, ketuk enter untuk kembali)")

print("Akhir dari program 1")

# contoh membuat exception
from numbers import Number

def tambah(a, b):
    if not isinstance(a, Number) or not isinstance(b, Number):
        raise "input harus angka"
    return a+b

print(tambah(5, 6))

angka = 0
try:
    hasil = 10 / angka

except Exception:
    input("(input tidak valid)")