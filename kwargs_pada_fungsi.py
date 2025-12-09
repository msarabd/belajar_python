'''***kwargs'''

def fungsi(nama, tinggi, berat):
    '''fungsi biasa'''
    print(F"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("Mahdi", 183, 65)

def fungsi(**kwargs):
    '''fungsi kwargs'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(F"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(nama="ucup", tinggi=183, berat=79)

# studi kasus

def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        print("operasi pertambahan")
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        print("operasi perkalian")
        for angka in args:
            output *= angka
    return output

print()
hasil = math(1,2,3,4,5,6,7,8,option="tambah")
print(f"hasil jumlah {hasil}")

print()
hasil = math(1,2,3,4,5,6,7,8,option="kali")
print(f"hasil kali {hasil}")