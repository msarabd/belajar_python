import os
from prettytable import PrettyTable

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
        while True:
            os.system("cls")
            print(5*"=", "Pertambahan", 5*"=", "\n")

            angka_1 = float(input("Masukkan angka pertama = "))
            angka_2 = float(input("Masukkan angka kedua = "))
            hasil = angka_1 + angka_2
            
            if hasil.is_integer() :
                print(f"Hasil dari {angka_1} ditambah {angka_2} adalah {int(hasil)}")

            else:
                print(f"Hasil dari {angka_1} ditambah {angka_2} adalah {round(hasil, 2)}")
            
            input("\n(Tekan enter untuk kembali)")
            break

    elif pilihan_1 == "2":
        while True:
            os.system("cls")
            print(5*"=", "Pengurangan", 5*"=", "\n")

            angka_1 = float(input("Masukkan angka pertama = "))
            angka_2 = float(input("Masukkan angka kedua = "))
            hasil = angka_1 - angka_2
            
            if hasil.is_integer() :
                print(f"Hasil dari {angka_1} dikurang {angka_2} adalah {int(hasil)}")

            else:
                print(f"Hasil dari {angka_1} dikurang {angka_2} adalah {round(hasil, 2)}")
            
            input("\n(Tekan enter untuk kembali)")
            break
    
    elif pilihan_1 == "3":
        while True:
            os.system("cls")
            print(5*"=", "Perkalian", 5*"=", "\n")

            angka_1 = float(input("Masukkan angka pertama = "))
            angka_2 = float(input("Masukkan angka kedua = "))
            hasil = angka_1 * angka_2

            if hasil.is_integer() :
                print(f"Hasil dari {angka_1} dikali {angka_2} adalah {int(hasil)}")

            else:
                print(f"Hasil dari {angka_1} dikali {angka_2} adalah {round(hasil, 2)}")
            
            input("\n(Tekan enter untuk kembali)")
            break
    
    elif pilihan_1 == "4":
        while True:
            os.system("cls")
            print(5*"=", "Pembagian", 5*"=", "\n")

            angka_1 = float(input("Masukkan angka pertama = "))
            angka_2 = float(input("Masukkan angka kedua = "))
            hasil = angka_1 / angka_2
            
            if hasil.is_integer() :
                print(f"Hasil dari {angka_1} dibagi {angka_2} adalah {int(hasil)}")

            else:
                print(f"Hasil dari {angka_1} dibagi {angka_2} adalah {round(hasil, 2)}")

            input("\n(Tekan enter untuk kembali)")
            break
    
    elif pilihan_1 == "5":
        while True:
            os.system("cls")
            print(5*"=", "Pengurangan", 5*"=", "\n")

            angka_1 = float(input("Masukkan angka pertama = "))
            angka_2 = float(input("Masukkan angka kedua = "))
            hasil = angka_1 - angka_2
            print(f"Hasil dari {angka_1} dikurang {angka_2} adalah {hasil}")
            input("\n(Tekan enter untuk kembali)")
            break

    elif pilihan_1 == "6":
        while True:
            os.system("cls")
            print(5*"=", "Pengurangan", 5*"=", "\n")

            angka_1 = float(input("Masukkan angka pertama = "))
            angka_2 = float(input("Masukkan angka kedua = "))
            hasil = angka_1 - angka_2
            print(f"Hasil dari {angka_1} dikurang {angka_2} adalah {hasil}")
            input("\n(Tekan enter untuk kembali)")
            break

    else:
        break

    #