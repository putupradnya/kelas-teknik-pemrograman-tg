def jumlah_total(harga, jumlah, diskon=0):
    total = (harga * jumlah) - (harga * jumlah * diskon)
    return total

harga = 50000
jumlah = 3
print(jumlah_total(harga, jumlah, diskon=0.1))