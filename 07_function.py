
def greeting(nama, umur):
    print("Halo kelas teknik pemrograman RTGD")
    print(f"Selamat datang ", nama, " umur kamu: ", umur)
    print("\n")

nama = ["Budi", "Susi", "Agus", "Lina", "RIna", "nadya"]
umur = [20, 21, 19, 22, 20, 21]

for i in range(len(nama)):
    greeting(nama[i], umur[i])