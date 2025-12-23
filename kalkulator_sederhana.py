import os
from prettytable import PrettyTable

def pertambahan():
    while True:
        os.system("cls")
        print(5*"=", "Pertambahan", 5*"=", "\n")

        try:
            angka_1 = float(input("Masukkan angka pertama = "))
            angka_2 = float(input("Masukkan angka kedua = "))
            hasil = angka_1 + angka_2
            
            if hasil.is_integer() :
                print(f"Hasil dari {angka_1} ditambah {angka_2} adalah {int(hasil)}")

            else:
                print(f"Hasil dari {angka_1} ditambah {angka_2} adalah {round(hasil, 2)}")
            
            input("\n(Ketuk enter untuk kembali)")
            break
    
        except Exception as e:
            input(f"\n({e}, ketuk enter untuk kembali)")

def pengurangan():
    while True:
        os.system("cls")
        print(5*"=", "Pengurangan", 5*"=", "\n")

        try:
            angka_1 = float(input("Masukkan angka pertama = "))
            angka_2 = float(input("Masukkan angka kedua = "))
            hasil = angka_1 - angka_2
            
            if hasil.is_integer() :
                print(f"Hasil dari {angka_1} dikurang {angka_2} adalah {int(hasil)}")

            else:
                print(f"Hasil dari {angka_1} dikurang {angka_2} adalah {round(hasil, 2)}")
            
            input("\n(Ketuk enter untuk kembali)")
            break

        except Exception as e:
            input(f"\n({e}, ketuk enter untuk kembali)")

def perkalian():
    while True:
        os.system("cls")
        print(5*"=", "Perkalian", 5*"=", "\n")

        try:
            angka_1 = float(input("Masukkan angka pertama = "))
            angka_2 = float(input("Masukkan angka kedua = "))
            hasil = angka_1 * angka_2

            if hasil.is_integer() :
                print(f"Hasil dari {angka_1} dikali {angka_2} adalah {int(hasil)}")

            else:
                print(f"Hasil dari {angka_1} dikali {angka_2} adalah {round(hasil, 2)}")
            
            input("\n(Ketuk enter untuk kembali)")
            break

        except Exception as e:
            input(f"\n({e}, ketuk enter untuk kembali)")

def pembagian():
    while True:
        os.system("cls")
        print(5*"=", "Pembagian", 5*"=", "\n")

        try:
            angka_1 = float(input("Masukkan angka pertama = "))
            angka_2 = float(input("Masukkan angka kedua = "))
            hasil = angka_1 / angka_2
            
            if hasil.is_integer() :
                print(f"Hasil dari {angka_1} dibagi {angka_2} adalah {int(hasil)}")

            else:
                print(f"Hasil dari {angka_1} dibagi {angka_2} adalah {round(hasil, 2)}")

            input("\n(Ketuk enter untuk kembali)")
            break

        except Exception as e:
            input(f"\n({e}, ketuk enter untuk kembali)")

while True:
    os.system("cls")
    tabel_menu = PrettyTable()
    tabel_menu.title = "MAU OPERASI APA GANTENG?"
    tabel_menu.field_names = ["kiri", "kanan"]
    tabel_menu.header = False
    tabel_menu.add_rows([
        ["[1]", "Pertambahan"],
        ["[2]", "Pengurangan"],
        ["[3]", "Perkalian"],
        ["[4]", "Pembagian"],
        ["[0]", "Keluar"]
    ])
    print(tabel_menu)
    pilihan_1 = input("Pilih menu (1-6) = ").strip()
    
    if pilihan_1 == "1":
        pertambahan()

    elif pilihan_1 == "2":
        pengurangan()
    
    elif pilihan_1 == "3":
        perkalian()
    
    elif pilihan_1 == "4":
        pembagian()

    elif pilihan_1 == "0":
        break

    else:
        input("\n(Input tidak valid, ketuk enter untuk memilih kembali)")
    