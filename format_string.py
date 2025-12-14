# format string

# contoh generic
# string
nama = "marle"
sapa_nama = f"hello {nama}"

print(sapa_nama)

# angka
angka = 2006.5
format_str = f"angka = {angka}"
print(format_str)

# boolean
bool = False
format_str = f"boolean = {bool}"
print(format_str) 

# bilangan bulat
angka = 25
format_str = f"angka = {angka}"
print(format_str)
 
# bilangan dengan ordo ribuan
angka = 2000000
format_str = f"angka = {angka:,}" # jadi ada koma, 2,000,000
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"angka = {angka: .2f}" # .2f = hanya tampil 2 angka di belakang koma
print(format_str)

# menampilkan leading zero
angka = 2503.54321
format_str = f"angka = {angka:09.3f}" # 0 artinya depannya ada 0, 9 artinya ada 9 karakter termasuk "."
print(format_str)

# menanmpilkan tanda + atau -
angka_minus = -5
angka_plus = 5
format_minus = f"minus = {angka_minus:-.3f}"
format_plus = f"plus= {angka_plus:+.2f}" # biar muncul tanda "+"

print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.453
format_persen = f"persen = {persentase:.2%}" # agar menunculkan tanda "%" dengan 2 angka di belakang koma
print(format_persen)

# melakukan operasi aritmatika di dalam plascehholder
harga = 2000
jumlah = 10
total_harga = f"total harga = Rp{harga*jumlah:,}"
print(total_harga)

# format angka lain (binary, octal, hexadimal)

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex= f"hex = {hex(angka)}"

print(format_binary + ", " + format_octal + ", " + format_hex)