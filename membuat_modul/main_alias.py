# module matematika dengan import

from matematika import tambah as tb
from matematika import kali as kl
from matematika import pangkat as pk

import matematika as math

hasil_tambah = tb(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = kl(1,2,3,4,5)
print(f"hasil kali = {hasil_kali}")

pangkat_2 = pk(2)
print(f"hasil pangkat = {pangkat_2(5)}")