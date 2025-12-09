# 1. mode write

# dia akan membuat file baru jika tidak ada,
# lalu akan menimpa atau overwrite isinya

with open("write_external_file\data.txt","w", encoding="utf-8") as file:
    file.write("Ucup si Rucup")

with open("write_external_file\data.txt","w", encoding="utf-8") as file:
    file.write("Jhon")

# 2. mode append

# kalau w, dia akan overwrite file terlebih dahulu
# kalau a, dia akan menambah saja dari file yang sudah ada
# kalau file belum ada, dia akan write seperti biasa

with open("write_external_file\data2.txt","a", encoding="utf-8") as file:
    file.write("Ucup si Rucup\n")

with open("write_external_file\data2.txt","a", encoding="utf-8") as file:
    file.write("Jhon\n")

with open("write_external_file\data2.txt","a", encoding="utf-8") as file:
    file.write("Mantap")

# 3. mode r+

with open("write_external_file\data3.txt","w", encoding="utf-8") as file:
    file.write("Mantap")

with open("write_external_file\data3.txt","r+", encoding="utf-8") as file:
    file.write("baris 1\n")
    file.write("baris 2\n")
    file.write("baris 3\n")

with open("write_external_file\data3.txt","r+", encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("write_external_file\data3.txt","r+", encoding="utf-8") as file:
    file.write("otong surotong") # menimpa isi text sesuai dengan panjang data

    