# operasi dan manipulasi string

# 1. Menyambung string (concatenate)
nama_pertama = "Monkey"
nama_kedua = "D"
nama_ketiga = "Luffy"

nama_lengkap = nama_pertama + " " + nama_kedua + "'" + nama_ketiga
print("nama lengkap =", nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. Operator untuk string

# mengecek apakah ada komponen char atau string di string

huruf = "D" # karakter "d" dan "D" itu berbeda
status = huruf in nama_lengkap
print("huruf " + huruf + " di " + nama_lengkap + " = " + str(status))

huruf = "d" 
status = huruf in nama_lengkap
print("huruf " + huruf + " di " + nama_lengkap + " = " + str(status))

huruf = "D" 
status = huruf not in nama_lengkap
print("huruf " + huruf + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk" * 10)
print(10 * "wk")

# indexing
print("index ke-7 : " + nama_lengkap[7]) # mulai dari 0
print("index terakhir : " + nama_lengkap[-1]) # negatif mulai dari belakang
print("index ke-0 sampai 3 : " + nama_lengkap[0:4]) # awal:akhir (akhir tidak termasuk)
print("index ke-7 sampai akhir : " + nama_lengkap[7:])
print("index ke-0,2,4,6 : " + nama_lengkap[0:7:2]) # awal:akhir:step

# item paling kecil 
print("paling kecil : " + min(nama_lengkap)) # ASCI codenya
# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII code 117 adalah " + chr(data))

# 4. Operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o") # .count() termasu method
print("jumlah o pada " + data + " " + str(jumlah))