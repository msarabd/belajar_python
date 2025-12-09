data_dict = {
    "cup" : "ucup surucup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung"
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"Panjang dictionary: {LENDICT}")

# mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis", "key tidak ditemukan")) # bedannya, kalau value yang dipanggil tidak ada, maka di terminal dia tidak error

# mengupdate data
print()
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "asep si kasyep"
print(data_dict)

data_dict.update({"cup" : "ucup surucup"})
print(data_dict)
data_dict.update({"faqih" : "faqihza si kweren"})
print(data_dict)

# mendelete data pada dictionary
del data_dict["faqih"]
print(data_dict)