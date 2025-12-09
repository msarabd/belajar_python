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

# looping first try

for data in data_pemain:
    print(data)

# operator untuk mengambil item / iterables
keys = data_pemain.keys()
print(keys)

for key in data_pemain.keys():
    print(data_pemain.get(key))

print()
values = data_pemain.values()
print(values)

print()
for value in data_pemain.values():
    print(value)

print()
items = data_pemain.items()
print(items)

print()
for item in data_pemain.items():
    print(item)

for key, value in data_pemain.items():
    for song in value:
        print(f"{song} = {key}")