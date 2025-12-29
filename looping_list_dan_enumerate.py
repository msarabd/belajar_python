# looping dari list

# for loop
print("FOR LOOP")
kumpulan_angka = [1,4,2,7,6,8]

for angka in kumpulan_angka:
    print(f"angka = {angka}") # mengambil komponen/element2 dari list

peserta = ["Antonio", "La Brava", 5]

for nama in peserta:
    print(f"nama = {nama}")

# for loop dan range
print("\nFOR LOOP DAN RANGE")
kumpulan_angka = [10,2,3,2,4,5]

for i in range(len(kumpulan_angka)):
    print(f"angka ke {i+1} = {kumpulan_angka[i]}") 

# while
print("\nWHILE LOOP")
kumpulan_angka = [10,2,3,2,4,5]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka ke {i+1} = {kumpulan_angka[i]}") 
    i += 1

# list comprehention
print("\nLIST COMPREHENTION")
data = [1,2,5,7,2]

[print(f"data = {i}") for i in data] # kayak dibalik aja format penulisan dari for loop biasanya

angka_kubik = [i**3 for i in data]
print(angka_kubik)

# enumerate
print("\nENUMERATE")
data_list = ["ucup", True, 5, 4, "Bro"]

for index, data in enumerate(data_list):
    print(f"data ke {index+1} = {data}") # enumerate itu untuk mengakses index dari data