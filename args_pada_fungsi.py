'''*args'''

# memasukkan data/argument

def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ucup", 170, 40)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    
fungsi(["otong", 100, 200])

# kenalan dengan *args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("dudung", 120, 120)

# studi kasus

def tambah(*data):
    # data tipenya adalah tuple, dia bisa diitersikan
    output = 0
    for angka in data:
        output += angka

    return output

hasil = tambah(100,200,300)
print(f"hasil = {hasil}")

data_list = [1, 3, 5]

def kali(data):
    output = 1
    for angka in data:
        output *= angka
    
    return output

hasil = kali(data_list)
print(f"hasil = {hasil}")