batas = int(input("Mau berapa baris = "))
kali = 1

"""
while True:
    print("*" * kali)
    if kali == batas:
        break
    kali += 1
"""
# membuat segitiga sama kaki
angka = 0
spasi = 0

if batas % 2 == 0:
    batas -= 1

while True:
    angka += 1
    if angka % 2 == 0:
        continue
    if angka > batas:
        break
    spasi += 1
    print(" " * (batas // 2 - (spasi - 1)), "+" * angka)

print()
# membuat belah ketupat
angka = 0
spasi = 0

if batas % 2 == 0:
    batas -= 1

while True:
    angka += 1
    if angka % 2 == 0:
        continue
    if angka > batas:
        angka -= 2
        while True:
            angka -= 1
            if angka % 2 == 0 and angka != 0:
                continue
            if angka == 0:
                break
            spasi -= 1
            print(" " * (batas // 2 - (spasi - 1)), "+" * angka)
        break
    spasi += 1
    print(" " * (batas // 2 - (spasi - 1)), "+" * angka)

# for i in range(batas):
#     print("* " * (i+1))
#     if i == batas:
#         break
