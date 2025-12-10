data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

"""
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote '...'
"""
data = 'ini adalah string'
print(data)

data = "ini adalah string"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\' day, isn\'t it?')

# backlash
print("C:\\user\\Ucup")

# tab
print("ucup \totong") # jadi jauhan

# backspace
print("ucup \botong") # jadi deketan

# newline
print("baris pertama.\nbaris kedua") # LF -> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua") # CR -> carriage return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua") # CRLF -> carriage return line feed -> 

# 3. String Literal atau raw

# hati-hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw string
print(r"C:\new folder")

# multiline literal string
print("""
Nama : Ucup
Kelas : XII RPL 1    
      """)

# multiline raw string
print(r"""
Nama : Ucup
Kelas : XII\RPL\1 
""")