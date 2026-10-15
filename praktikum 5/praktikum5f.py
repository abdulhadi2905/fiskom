
# MENENTUKAN LAMA PELURU MELAYANG DI UDARA
# Metode Newton-Raphson

import math

# Membaca data awal
vo = float(input("Masukkan kecepatan awal (m/s): "))
alpha = float(input("Masukkan sudut elevasi (derajat): "))
t = float(input("Masukkan nilai awal waktu (s): "))

g = 9.81
imax = 15

# Mengubah sudut derajat menjadi radian
sudut = alpha * math.pi / 180

# Iterasi Newton-Raphson
print("\nHasil Iterasi Newton-Raphson")
print(f"{'N':<10}{'t (s)':<20}{'Error':<20}")

for n in range(1, imax + 1):

    # Fungsi posisi vertikal peluru
    ft = vo * math.sin(sudut) * t - 0.5 * g * t**2

    # Turunan fungsi terhadap waktu
    dft = vo * math.sin(sudut) - g * t

    # Memeriksa turunan agar tidak dibagi nol
    if abs(dft) < 1e-12:
        print("Turunan mendekati nol. Iterasi dihentikan.")
        break

    # Menghitung waktu pendekatan berikutnya
    t_baru = t - ft / dft

    # Menghitung error
    error = abs(t_baru - t)

    print(f"{n:<10}{t_baru:<20.10f}{error:<20.10f}")

    # Memperbarui nilai waktu
    t = t_baru

    # Menghentikan iterasi jika sudah konvergen
    if error < 1e-10:
        break

# Menampilkan lama peluru di udara
if t > 0:
    print("\nLama peluru melayang =", t, "sekon")
else:
    print("\nHasil bukan waktu terbang positif.")
    print("Coba gunakan nilai awal waktu yang berbeda.")
