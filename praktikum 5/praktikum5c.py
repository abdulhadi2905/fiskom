# METODE NEWTON-RAPHSON ORDE-N
# Berdasarkan flowchart akar polinom

# Membaca orde polinomial dan jumlah iterasi
n = int(input("Masukkan orde polinomial: "))
imax = int(input("Masukkan jumlah iterasi: "))

# Membaca koefisien polinomial dari pangkat tertinggi
# sampai konstanta
a = [0.0] * (n + 2)

for j in range(1, n + 2):
    a[j] = float(input(f"Masukkan koefisien a({j}): "))

# Membaca nilai awal
z = float(input("Masukkan nilai awal x: "))

print("\nHasil Iterasi Newton-Raphson")
print(f"{'Iterasi':<10}{'x':<20}{'f(x)':<20}{'Error':<20}")

# Proses iterasi
for i in range(1, imax + 1):

    # Menghitung nilai f(z) dan f'(z) sekaligus menggunakan Skema Horner
    fz = a[1]
    dz = a[1]

    for j in range(2, n + 1):
        fz = fz * z + a[j]
        dz = dz * z + fz

    fz = fz * z + a[n + 1]

    # Memeriksa turunan agar tidak dibagi nol
    if dz == 0:
        dz += 0.01  # Menambahkan nilai kecil untuk menghindari pembagian nol

    # Menghitung pendekatan akar berikutnya
    x_baru = z - fz / dz

    # Menghitung error
    error = abs(x_baru - z)

    # Menampilkan hasil iterasi
    print(f"{i:<10}{x_baru:<20.10f}{fz:<20.10f}{error:<20.10f}")

    # Memperbarui nilai pendekatan
    z = x_baru

# Menampilkan akar pendekatan terakhir
print("\nAkar pendekatan =", z)