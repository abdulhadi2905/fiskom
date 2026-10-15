
# METODE PEMBAGIAN SINTETIK
# Menentukan akar polinomial

# Membaca orde polinomial
n = int(input("Masukkan orde polinomial: "))

# Membaca koefisien dari pangkat tertinggi
# sampai konstanta
a = []

for i in range(n + 1):
    koef = float(input(f"Masukkan koefisien x^{n-i}: "))
    a.append(koef)

# Kandidat akar rasional untuk contoh polinomial
kandidat = [
    12, -12, 6, -6, 4, -4, 3, -3,
    2, -2, 1, -1, 0.5, -0.5,
    1.5, -1.5, 2.5, -2.5
]

akar = []

# Pembagian sintetik berulang
while len(a) > 2:

    ditemukan = False

    for r in kandidat:

        # Proses pembagian sintetik
        b = [0.0] * len(a)
        b[0] = a[0]

        for j in range(1, len(a)):
            b[j] = a[j] + r * b[j-1]

        # Sisa pembagian adalah elemen terakhir
        sisa = b[-1]

        if abs(sisa) < 1e-9:

            # r merupakan akar polinomial
            akar.append(r)

            print("\nAkar ditemukan:", r)
            print("Tabel pembagian sintetik:")

            for nilai in b:
                print(f"{nilai:10.4f}", end=" ")
            print()

            # Koefisien baru adalah hasil bagi
            a = b[:-1]

            print("Koefisien polinomial hasil bagi:", a)

            ditemukan = True
            break

    if not ditemukan:
        print("\nAkar rasional tidak ditemukan.")
        print("Koefisien terakhir:", a)
        break

# Jika tersisa polinomial linear
if len(a) == 2:
    if abs(a[0]) > 1e-9:
        r = -a[1] / a[0]
        akar.append(r)
        print("\nAkar terakhir:", r)

# Menampilkan semua akar
print("\nSemua akar polinomial:")
for i, r in enumerate(akar, start=1):
    print(f"x{i} = {r:g}")
