# program list buku

import os 

data_buku = []

token = False
while not token:
    try: 
        judul = input("Masukkakan judul buku = ").strip()
        penulis = input("Masukkan nama penulis = ").strip()

        data_buku.append([judul, penulis])
        print("\n", 5*"=", "DATA BUKU", 5*"=")
        
        for i, data in enumerate(data_buku):
            # print(f"\nBuku {i+1}")
            # print(f"Judul = {data[0]}")
            # print(f"Penulis = {data[1]}")
            print(f"{i+1} | {data[0]} | {data[1]} ")

        pilihan_1 = input("\nIngin lanjut (y/t)? ").strip()
        print()
        
        while True:
            if pilihan_1 == "y":
                os.system("cls")                
                break

            elif pilihan_1 == "t":
                token = True
                break

            
            else:
                pilihan_1 = input("Ingin lanjut (y/t)? ").strip()
                print()
                continue
    
    except Exception as e:
        input(f"({e})")

print("Terima kasih")