# copy dictionary
data_pemain = {
    "gk_utama" : ["Marten Paes"],
    "df_utama" : ["Jay Idzes",
                  "Rizky Ridho",
                  "Justin Hubner", 
                  "Calvin Verdonk", 
                  "Kevin Diks"
                  ],
    "mf_utama" : ["Thom Haye",
                  "Joel Pelupessy", 
                  "Marselino"
                  ],
    "fw_utama" : ["Rafael Struick",
                  "Ole Romeny"
                  ],
    "gk_cadangan" : ["Emil Audero",
                     "Nadeo Argawinata"
                     ],
    "df_cadangan" : ["Mees Hilgers",
                     "Sandy Walsh",
                     "Yakob Sayuri",
                     "Yance Sayuri",
                     "Justin Hubner"
                     ],
    "mf_cadangan" : ["Ivar Jenner",
                     "Ricky Kambuaya"
                     ],
    "fw_cadangan" : ["Ragnar Oratmangoen",
                     "Miliano Jonathans",
                     "Egy Maulana Vikry"
                     ],
}

punggawa = data_pemain.copy()

print(f"data pemain = {data_pemain}\n")
print(f"punggawa = {punggawa}\n")

data_pemain["gk_utama"] = ["Mahdi", "Arya"]
print(f"data pemain = {data_pemain}\n")
print(f"punggawa = {punggawa}\n") # saat dic data_pemain diubah, dic punggawa tidak akan ikut berubah

# pop dictionary (berdasarkan key)
timnas = data_pemain["gk_utama"].pop(1)
print(f"data timnas = {timnas}\n")
print(f"gk utama = {data_pemain}\n")

# popitem dictionary (yang terakhir saja)
timnas = data_pemain.popitem()
print(f"data timnas = {timnas}\n")
print(f"data pemain = {data_pemain}\n")

