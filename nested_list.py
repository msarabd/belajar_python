data_list_biasa = [1,2,3,4,5]
print(f"List biasa = {data_list_biasa}")

data_0 = [1,2]
data_1 = [3,4,5]
list_2d = [data_0, data_1, 5, 7, 8]
print(f"List 2d = {list_2d}")

# Contoh penggunaan

peserta_0 = ["ucup", 25, "laki-laki"]
peserta_1 = ["mahdi", 20, "laki-laki"]
peserta_2 = ["neytri", 16, "perempuan"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"{list_peserta}\n")

for peserta in list_peserta:
    print("Nama", peserta[0])
    print("Umur", peserta[1])
    print("Gender", peserta[2], "\n")

# Dengan refrence

list_copy = list_peserta.copy()
print(f"Sebelum list_copy = {list_copy}")
list_peserta[0][0] = "michel"
print(f"Sesudah list_copy = {list_copy}") # saat data list asli nya diubah, data copy-an juga ikut betubah
