import os

input("test")

# di bawah ini berfungsi jika file ini di import ke file atau moodule lain, maka semua yang ada pada
# percabangan ini tidak akan dijalankan
if __name__ == "__main__": # meskipun nama file bukan main, tetap tulis __main__
    sistem_operasi = os.name

    match sistem_operasi: # kurang lebih aja sama if-else
        case "posix": os.system("clear")
        case "nt": os.system("cls")