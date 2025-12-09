# Fungsi dengan kembalian

# template fungsi dengan kembalian
# deg nama_fungsi(argument):
#   badan_fungsi
#   return output

# fungsi kuadrat

def kuadrat(x):
    hasil = x ** 2
    volume = x ** 3
    return hasil

print(kuadrat(10))

z = 10 + kuadrat(7)
print(z)

def fungsi_tambah(angka_1, angka_2):
    return angka_1 + angka_2

a = fungsi_tambah(10, 10)
print(a)

# fungsi dengan return banyak

def operasi_matematika(angka_1, angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    print("hello")
    return tambah, kurang, kali, bagi

print(operasi_matematika(10,5))
k,l,m,n = operasi_matematika(10, 5)

print(f"Hasil tambah = {k}")    
print(f"Hasil kurang = {l}")    
print(f"Hasil kali = {m}")    
print(f"Hasil bagi = {n}")    
