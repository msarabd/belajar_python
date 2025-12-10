# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# ++++++3------------10++++++

input_a = float(input("masukkan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10: "))

# ++++++3------------
# memeriksa angka kurang dari 3
kurangDari = (input_a < 3) # var yang dikomparasikan harus bertipe float
print(f"kurang dari 3: {kurangDari}")

# ------------10++++++
# memeriksa angka lebih besar dari 10
lebihDari = (input_a > 10)
print(f"lebih dari 10: {lebihDari}")

# ++++++3------------10++++++

hasilDari = kurangDari or lebihDari
print(f"kurang dari 3 atau lebih dari 10: {hasilDari}")

# ------3++++++10------
# kasus irisan

print("\n", 10*"=", "\n")
input_b = float(input("masukkan angka yang bernilai \nlebih dari 3 \ndan \nkurang dari 10: "))

# ------3++++++
# memeriksa angka lebih dari 3
lebihDari = (input_b > 3) # var yang dikomparasikan harus bertipe float
print(f"lebih dari 3: {lebihDari}")

# ++++++10------
# memeriksa angka kurang dari 10
kurangDari = (input_b < 10)
print(f"kurang dari 10: {kurangDari}")

# ++++++3------------10++++++

hasilDari = lebihDari and kurangDari
print(f"lebih dari 3 dan kuarng dari 10: {hasilDari}")

## soal latihan
# ------0++++++5-------8++++++11------

print("\n", 10*"=", "\n")
input_c = float(input("masukkan angka yang bernilai \nlebih dari 0 dan kurang dari 5 \natau \nlebih dari 8 dan kurang dari 11: "))

# ------0++++++5--------
cekPertama = input_c > 0 and input_c < 5
print(f"lebih dari 0 dan kuarng dari 5: {cekPertama}")

# -------8++++++11------
cekKedua = input_c > 8 and input_c < 11
print(f"lebih dari 8 dan kurang dari 11: {cekKedua}")

# ------0+++++++5+++++++8------11++++++
hasilDari = cekPertama or cekKedua
print(f"lebih dari 0 dan kurang dari 5 \natau \nlebih dari 8 dan kuarng dari 11: {hasilDari}")

# ++++++0------5+++++++8------11++++++

print("\n", 10*"=", "\n")
input_d = float(input("masukkan angka yang bernilai \nkurang dari 0 \natau \nlebih dari 5 dan kurang dari 8 \natau \nlebih dari 11: "))

# ++++++0------
cekPertama = input_d < 0
print(f"kurang dari 0: {cekPertama}")

# -------5+++++++8------
cekKedua = input_d < 8 and input_d > 5
print(f"lebih dari 5 dan kurang dari 8: {cekKedua}")

# ++++++11------
cekKetiga = input_d > 11
print(f"lebih dari 11: {cekKetiga}")

# ++++++0------5+++++++8------11++++++
hasilDari = cekPertama or cekKedua or cekKetiga
print(f"kurang dari 0 \natau \nlebih besar dari 5 dan kurang dari 8 \natau \nlebih dari 11: {hasilDari}")


