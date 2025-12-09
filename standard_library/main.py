import datetime

data_waktu = datetime.datetime.now()
print(f"datetime now : {data_waktu}")
print(f"tahun : {data_waktu.year}")
print(f"bulan : {data_waktu.month}")
print(f"tanggal : {data_waktu.day}")
print(f"hari : {data_waktu.strftime("%A")}")

from collections import Counter

data = ["a", "b", "c", "c", "c", "a", "b", "a"]
data_count = Counter(data)

print(f"data count = {data_count}")
print(f"jumlah 'a' = {data_count["a"]}")

import io

file = io.open("file_text.txt","r")
print(file.read)

