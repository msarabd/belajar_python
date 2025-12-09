# Lambda function

def kuadrat(angka):
    return angka**2

x = 2
print(f"hasil fungsi kudrat dari {x} = {kuadrat(x)}")

# kita coba dengan lambda
# output = lambda argument: expression

kuadrat = lambda angka: angka**2
x = 2
print(f"hasil fungsi kudrat dari {x} = {kuadrat(x)}")

pangkat = lambda num, pow: num**pow
print(f"hasil dari fungsi pangkat = {pangkat(4, 2)}")

## kegunaannya apa bang?

# sorting untuk list biasa
data_list = ["otong", "ucup", "dudung"]
data_list.sort()
print(f"sorted list = {data_list}")

# sorting dia pakai panjang
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"sorted list by panjang nama = {data_list}")

# sort pakai lambda
data_list = ["otong", "ucup", "dudung"]
data_list.sort(key=lambda nama: len(nama))
print(f"sorted list by lambda = {data_list}")

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurang_dari_lima(angka):
    return angka < 5

data_angka_baru = list(filter(kurang_dari_lima, data_angka))
data_angka_baru = list(filter(lambda x: x < 5, data_angka))
print(data_angka_baru)

# kasus genap
data_genap = list(filter(lambda x: x % 2 == 0, data_angka))
print(data_genap)

# kasus ganjil
data_ganjil = list(filter(lambda x: x % 2 == 1, data_angka))
print(data_ganjil)

# kelipatan 4
data_kel_4 = list(filter(lambda x: x % 4 == 0, data_angka))
print(data_kel_4)

# anonymous function
# currying <- Haskell Curry

def pangkat(angka, n):
    hasil = angka ** n
    return hasil

data_hasil = pangkat(5,2)
print(f"fungsi biasa = {data_hasil}")

# dengan currying menjadi

def pangkat(n):
    return lambda angka: angka ** n

pangkat2 = pangkat(2)
print(f"pangkat 2 dari 5 = {pangkat2(5)}")

pangkat3 = pangkat(3)
print(f"pangkat 3 dari 5 = {pangkat3(5)}")

print(f"pangkat bebas dari 5 = {pangkat(4)(5)}")

