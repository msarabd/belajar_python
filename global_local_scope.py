## Global dan local scope

nama_global = "otong" # -> ini adalah var global

# akses variabel global dalam fungsi
def fungsi():
    print(f"fungsi menampilkan {nama_global}")

fungsi()

# akses variabel global dalam loop
for i in range(1,6):
    print(f"loop {i} - {nama_global}")

# percabangan
if True:
    print(f"if menampilkan {nama_global}")

## variabel lokal scope

def fungsi2():
    nama_local = "ucup" # -> variabel lokal scope

fungsi2()
# print(nama_local) # tidak bisa dilakukan

## contoh 1: penggunaan  akses variabel

def say_otong():
    print(f"Hello {nama}")

nama = "Mahdi" # var bisa dipanggil setelah membuat def asal letaknya sebelum pemanggilan fungsinya
say_otong()

## contoh 2: merubah variabel global
angka = 0

def rubah_angka(nilai_baru):
    global angka # fungsi ini mendapat akses merubah variabel global
    angka = nilai_baru 
    return angka

print(f'sebelum {angka}')
rubah_angka(10)
print(f'sesudah {angka}')

## contoh 3:
angka = 0

for i in range(0, 5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 100
    angka_dummy = 200

print(angka)
print(angka_dummy)
