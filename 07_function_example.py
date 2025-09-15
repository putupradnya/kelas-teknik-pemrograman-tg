def jumlah(*args):
    total = 0
    for i in args:
        total += i
    return total

print(jumlah(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))