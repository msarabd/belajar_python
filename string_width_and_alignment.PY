# Width and Multiline

# Data

data_nama = "Mahdi Ganteng"
data_umur = 19
data_tinggi = 165.5
data_nomor_sepatu = 43

# string standard
print(5*"=", "DATA STRING", 5*"=")
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi:.3f} cm, ukuran sepatu = {data_nomor_sepatu}" # {} -> ini namanya placeholder
print(data_string)

# string multiline (dengan menggunakan enter, newline, \n)
print("\n" + 5*"=", "DATA STRING", 5*"=")
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi:.3f} cm, \nukuran sepatu = {data_nomor_sepatu}"
print(data_string)

# string multiline (kutip triplets)
print("\n" + 5*"=", "DATA STRING", 5*"=")
data_string = f"""nama = {data_nama},
umur = {data_umur},
tinggi = {data_tinggi:.3f} cm,
ukuran sepatu = {data_nomor_sepatu}"""
print(data_string)

# mengatur lebar
print("\n" + 5*"=", "DATA STRING", 5*"=")
data_nama = "Mahdi"
data_string = f"""nama    = {data_nama:>10}
umur    = {data_umur:>10}
tinggi  = {data_tinggi:>10}
sepatu  = {data_nomor_sepatu:>10}""" # agar saama ada 10 karakter di sebelah "="
print(data_string)

