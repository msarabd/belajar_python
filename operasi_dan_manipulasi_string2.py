# operator dalam bentuk method

## merubah case dari string

# merubah semua ke upper case

salam = "bro!"
print("normal =", salam)
salam = salam.upper()
print("upper =", salam)

# merubah semua ke lower case

print("====================")
salam = "HALO!"
print("normal =", salam)
salam = salam.lower()
print("lower =", salam)

## pengecekan dengan isX method

# contoh pengecekan lower case dan upper case
salam = "test"
apakah_lower = salam.islower() # hasilnya bool
print("apakah " + salam + " adalah lower ? " + str(apakah_lower)) 
apakah_upper = salam.isupper() # hasilnya bool
print("apakah " + salam + " adalah upper ? " + str(apakah_upper)) 

# isalpha() -> untuk mengecek semuanya huruf
data = "asel ole 12"
apakah_alpha = data.isalpha()
print("apakah " + data + " semuanya huruf ? " + str(apakah_alpha))
# isalnum() -> hanya huruf atau angka
apakah_alnum = data.isalnum()
print("apakah " + data + " ada huruf atau angka ? " + str(apakah_alnum))
# isdecimal() -> hanya angka
apakah_decimal = data.isdecimal()
print("apakah " + data + " semuanya angka ? " + str(apakah_decimal))
# isspace() -> hanya spasi, tab, newline
apakah_space = data.isspace()
print("apakah " + data + " ada spasi, tab, newline ? " + str(apakah_space))
# istitle() -> semua kata dimulai dengan huruf besar
data = "Ini adalah Maut"
apakah_title = data.istitle()
print("apakah " + "\"" + data + "\"" + " semua katanya dimulai dengan kapital ? " + str(apakah_title))

## ngecek komponen startswith() endwith() <-- keren
cek_start = "Kilian Mbappe".startswith("Kilian") # bisa langsung dikasih method di akhir string
print("starts = " + str(cek_start))
cek_end = "Kilian Mbappe".endswith("appe")
print("ends = " + str(cek_end))

## penggabungan komponen join() dan split()
pisah = ["aku", "sayang", "kamu"]
print(pisah)

gabungan = " ".join(pisah)
print(gabungan)

gabungan = ",".join(pisah)
print(gabungan)

gabungan = " ehm".join(pisah)
print(gabungan)

gabungan = "aku sayang kamu".split(" ")
print(gabungan)

# alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'" + kanan + "'") # total karakter sebelum "kanan" ada 10

kiri = "kiri".ljust(10)
print("'" + kiri + "'") # total karakter sesudah "kiri" ada 10

tengah = "tengah".center(20,"@") # kalau mau di sebelahnya bukan spasi
print("'" + tengah + "'") # total karakter sesudah dan sebelum "tengah" ada 10/2 = 5

# kebalikannya -> strip()
tengah = tengah.strip("@") # untuk menghapus karakter tertentu di kiri dan kanan
print("'" + tengah + "'")