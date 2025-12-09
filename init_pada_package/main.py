import package

hasil_tambah = package.matematika.tambah(1,2,3,4,5,6)
print(f"hasil tambah = {hasil_tambah}")

hasil_fisika = package.fisika.gaya(10,9.8)
print(f"hasil fisika = {hasil_fisika}")

hasil_kali = package.kali(2, 5)
print(f"hasil kali = {hasil_kali}")

# from package import * # hanya bisa dipakai saat pakai __all__ di init

# hasil_tambah = matematika.tambah(1,2,3,4,5,6)
# print(f"hasil tambah = {hasil_tambah}")

# hasil_fisika = fisika.gaya(10,9.8)
# print(f"hasil fisika = {hasil_fisika}")