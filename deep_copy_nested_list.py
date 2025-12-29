data_0 = [1,2]
data_1 = [3,4]

data_2d = [data_0, data_1, 9]
data_2d_copy = data_2d.copy()
print(f"data = {data_2d}")
print(f"data copy = {data_2d_copy}")

# Mengambil data dari nested list

data = data_2d[0][1]
print(f"\ndata = {data}")

# address semuanya

print(f"\ndata asli = {hex(id(data_2d))}")
print(f"data copy = {hex(id(data_2d_copy))}")

print("\naddress dari member ke-1")
print(f"data asli = {hex(id(data_2d[0]))}")
print(f"data copy = {hex(id(data_2d_copy[0]))}") # address member ke-1 yang asli dan copy sama

data_2d[0][1] = 5
print(f"\ndata = {data_2d}")
print(f"data copy = {data_2d_copy}") # kalau yang diubah adalah elemen yang berbentuk list, maka dia akan ikut berubah

data_2d[2] = 100
print(f"\ndata = {data_2d}")
print(f"data copy = {data_2d_copy}") # kalau yang diubah adalah elemen tidak berbentuk list, maka dia tidak akan ikut berubah

# ini adalah implementasi shallow copy (salinan dangkal), saat membernya list dia akan meng-copy address
# sedangkan kalau membernya berbentuk angka, dia akan meng-copy angka

# kita gunakan deepcopy

from copy import deepcopy

data_2d_deepcopy = deepcopy(data_2d)

print(f"\ndata asli = {hex(id(data_2d))}")
print(f"data deepcopy = {hex(id(data_2d_deepcopy))}") # sama kyk shallow copy, addrres antar asli dan copy berbeda

print("\naddress dari member ke-1")
print(f"data asli = {hex(id(data_2d[0]))}")
print(f"data deepcopy = {hex(id(data_2d_deepcopy[0]))}") # address member ke-1 yang asli dan copy berbeda

data_2d[0][1] = 90
print(f"\ndata = {data_2d}")
print(f"data deepcopy = {data_2d_deepcopy}") # tidak akan ikut berubah, karena dia berbeda address