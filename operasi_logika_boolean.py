# operasi logika atau boolean

# not, or, and, xor

# NOT
print("==== NOT ====")
a = True
c = not a
print("data a =", a)
print("============= NOT")
print("data c =", c)

# OR (jika salah satu saja ada True, maka hasil akan True)
print("\n==== OR ====")
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)

a = False
b = True
c = a or b
print(a, "OR", b, "=", c)

a = True
b = False
c = a or b
print(a, "OR", b, "=", c)

a = True
b = True
c = a or b
print(a, "OR", b, "=", c)

# AND (harus semua True, agar hasil True)
print("\n==== AND ====")
a = False
b = False
c = a and b
print(a, "AND", b, "=", c)

a = False
b = True
c = a and b
print(a, "AND", b, "=", c)

a = True
b = False
c = a and b
print(a, "AND", b, "=", c)

a = True
b = True
c = a and b
print(a, "AND", b, "=", c)

# XOR (kalau berbeda tanda, hasilnya akan True)
print("\n==== XOR ====")
a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c)

a = False
b = True
c = a ^ b
print(a, "XOR", b, "=", c)

a = True
b = False
c = a ^ b
print(a, "XOR", b, "=", c)

a = True
b = True
c = a ^ b
print(a, "XOR", b, "=", c)
