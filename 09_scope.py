# def hitung():
#     angka = 5  # local scope
#     print(f"nilai angka di dalam function: {angka}")

# jumlah = angka + 5
# print(jumlah)
# # hitung()

x = 10 # global scope

def panggil():
    global x
    x = 5
    print(x)

panggil()