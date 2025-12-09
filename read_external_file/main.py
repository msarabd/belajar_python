## Tutorial membaca file external

print(3*"=", " Membaca file txt ", 3*"=")
file = open("D:/belajar-python/read_external_file/data.txt", mode="r")

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")

## baca seluruh file
# print(file.read())

## baca per baris
print(file.readline(), end="")

## baca semua baris sebagai list
print(file.readlines())

print(f"apakah file suda diclosed : {file.closed}")
file.close() # harus ditutup biar tidak error
print(f"apakah file suda diclosed : {file.closed}")

## salah satu teknik membuka file di python
print("\n", 3*"=", " Membaca file txt dengan with ", 3*"=")

with open("D:/belajar-python/read_external_file/data.txt", mode="r") as file:
    content = file.readline()
    print(content, end="")
    print(f"apakah file suda diclosed : {file.closed}") # menggunakan with tidak perlu di closed, karena sudah otomatis closed

print(f"apakah file suda diclosed : {file.closed}")