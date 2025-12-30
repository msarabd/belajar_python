## operasi

# index 0(-3) | 1(-2) | 2(-1)

data = ["Septian", "Bagas", "Kara"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data/elemen pertama (index 0)= {data_0}")

data_terakhir = data[-1]
print(f"data/elemen terakhir (index-1) = {data_terakhir}")

data_septian = data[-3]
print(f"data Septian = {data_septian}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(F"panjang data = {panjang_data}")

## manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"\nlist data lama = \n{data}")
data.insert(1, "Daffa") # (index, value)
print(f"list data baru = \n{data}")

# menambah di akhir list
data.append("Jajang")
print(f"\nlist data baru = \n{data}")

# menambahkan list dengan list 
data_tambah = [5, 6, 7]
data.extend(data_tambah) # masukkan list data_tambah ke dalam list data
print(f"\nlist data tambahan = \n{data_tambah}")
print(f"list data baru = \n{data}")

## merubah data
# kita ubah data 2
data[2] = "ALpedo"
print(f"\nlist data baru = \n{data}")

# meremove data 
data.remove("Daffa") # kalau tau isi datanya
print(f"\nlist data baru = \n{data}")

data_akhir = data.pop()
print(f"\nlist data baru = \n{data}")
print("data akhir = ", data_akhir)

del data[2] # kalau tau index datanya
print(f"\nlist data baru = \n{data}")





