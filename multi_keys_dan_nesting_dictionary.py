import datetime

mahasiswa1 = {
    'nama':"Mantap Jiwa",
    'nim':'12345602',
    'sks':130,
    'beasiswa':False,
    'lahir':datetime.datetime(2006,1,5)
}

mahasiswa2 = {
    'nama':"Rijali",
    'nim':'12345603',
    'sks':130,
    'beasiswa':False,
    'lahir':datetime.datetime(2005,8,19)
}

mahasiswa3 = {
    'nama':"Kopiria",
    'nim':'12345604',
    'sks':130,
    'beasiswa':False,
    'lahir':datetime.datetime(2006,1,7)
}

data_mahasiswa ={
    'MAH01':mahasiswa1,
    'MAH02':mahasiswa2,
    'MAH03':mahasiswa3
}

print(f"{'KEY':<6} {'NAMA':<17} {'SKS':<3} {'BEASISWA':<9} {'LAHIR':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
    key = mahasiswa

    nama = data_mahasiswa[key]['nama']
    nim = data_mahasiswa[key]['nim']
    sks = data_mahasiswa[key]['sks']
    beasiswa = data_mahasiswa[key]['beasiswa']
    lahir = data_mahasiswa[key]['lahir'].strftime("%x")
    
    print(f"{key:<6} {nama:<17} {sks:<3} {beasiswa:^9} {lahir:<10}")
    