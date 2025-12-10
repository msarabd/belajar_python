# bitwise = operasi masing-masing bit

a = 9 
b = 5

# bitwise OR (|)
c = a | b
print("\n==========OR==========")
print(f"nilai: {a}, binary: {format(a,"08b")}") # "08b" = menampilkan data dalam lebar 8 biner digit dengan padding 0 di depan
print(f"nilai: {b}, binary: {format(b,"08b")}")
print("-----------------------(|)")
print(f"nilai: {c}, binary: {format(c, "08b")}")

# bitwise AND (&)
c = a & b
print("\n==========AND==========")
print(f"nilai: {a}, binary: {format(a,"08b")}")
print(f"nilai: {b}, binary: {format(b,"08b")}")
print("-----------------------(&)")
print(f"nilai: {c}, binary: {format(c, "08b")}")

# bitwise XOR (^)
c = a ^ b
print("\n==========XOR==========")
print(f"nilai: {a}, binary: {format(a,"08b")}")
print(f"nilai: {b}, binary: {format(b,"08b")}")
print("-----------------------(^)")
print(f"nilai: {c}, binary: {format(c, "08b")}")

# bitwise NOT (~)
c = ~a
print("\n==========NOT==========")
print(f"nilai: {a}, binary: {format(a,"08b")}")
print("-----------------------(~)")
print(f"nilai: {c}, binary: {format(c, "08b")}") # kalau a = 9, maka c = -10

# shifting

# shifting right (>>)
c = a >> 4 # geser ke kanan 4 bit
print("\n==========>>==========")
print(f"nilai: {a}, binary: {format(a,"08b")}")
print("-----------------------(>>)")
print(f"nilai: {c}, binary: {format(c, "08b")}") # kalau a = 9, maka c = -10

# shifting right (<<)
c = a << 4 # geser ke kiri 4 bit
print("\n==========<<==========")
print(f"nilai: {a}, binary: {format(a,"08b")}")
print("-----------------------(<<)")
print(f"nilai: {c}, binary: {format(c, "08b")}") # kalau a = 9, maka c = -10
