# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditamabah dengann assignment

a = 5 # adalah assignment
print("nilai a:", a)

a += 1 # artinya adalah a = a + 1
print("nilai a += 1, nilai a menjadi", a)

a -= 2 # artinya adalah a = a - 2
print("nilai a -= 2, nilai a menjadi", a)

a *= 5 # artinya adalah a = a * 5
print("nilai a *= 5, nilai a menjadi", a)

a /= 2 # artinya adalah a = a / 2
print("nilai a /= 2, nilai a menjadi", a)

# modulus dan floor division
b = 10
print("\nnilai b =", b)

b %= 3 # artinya adalah b = b % 3
print("nilai b %= 3, nilai b menjadi", b)

b = 10
print("\nnilai b =", b)

b //= 3 # artinya adalah b = b // 3
print("nilai b //= 3, nilai b menjadi", b)

a = 5
print("\nnilai a =", b)

a **= 3 # artinya adalah a = a ** 3
print("nilai a **= 3, nilai a menjadi", a)

# operasi bitwise
# OR
c = False
print("\nnilai c =", c)

c |= True # artinya adalah c = c | False
print("nilai c |= True, nilai c menjadi", c)

# AND
c = True
print("\nnilai c =", c)

c &= False # artinya adalah c = c & False
print("nilai c &= False, nilai c menjadi", c)

# geser geser
# geser ke kanan
d = 0b1100
print("\nnilai d =", format(d, "08b"))

d >>= 2 # artinya adalah d = d >> 2
print("nilai d >>= 2, nilai d menjadi", format(d, "08b"))

# geser ke kiri
d = 0b1100
print("\nnilai d =", format(d, "08b")) # 08b = menampilkan data dalam lebar 8 bit dengan padding 0 di depan

d <<= 2 # artinya adalah d = d << 2
print("nilai d <<= 2, nilai d menjadi", format(d, "08b"))
