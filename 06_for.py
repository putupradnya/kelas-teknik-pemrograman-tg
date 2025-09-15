nilai = [70, 80, 90, 60, 85, 75]

jumlah = 0
# cara loop pertama
# for i in nilai:
#     print(i)
#     jumlah += i

for i in range(start=0, stop=len(nilai), step=2):
    print(nilai[i])
    jumlah += nilai[i]

print(f"jumlah nilai = {jumlah}")