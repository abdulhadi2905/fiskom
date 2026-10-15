
# SIMULASI PARTIKEL DALAM SUMUR POTENSIAL BERHINGGA
# Metode Euler

import math
import matplotlib.pyplot as plt

# Parameter partikel dan sumur potensial
m = 1.0e-27       # Massa partikel (kg)
V0 = 1.0e-19      # Kedalaman sumur potensial (J)
L = 1.0e-9        # Setengah lebar karakteristik sumur (m)

# Kondisi awal
x = -2.0e-9       # Posisi awal (m)
v = 1.0e4         # Kecepatan awal (m/s)

# Parameter waktu
dt = 1.0e-16      # Langkah waktu (s)
tmax = 1.0e-12    # Waktu simulasi (s)
jumlah = int(tmax / dt)

# Menyimpan hasil simulasi
waktu = []
posisi = []
kecepatan = []
energi = []

# Proses simulasi metode Euler
for i in range(jumlah + 1):

    t = i * dt

    # Menghitung potensial pada posisi x
    rasio = x / L
    V = -V0 * math.exp(-(rasio**8))

    # Menghitung gaya F(x) = -dV/dx
    F = -(8 * V0 * x**7 / L**8) * math.exp(-(rasio**8))

    # Menghitung energi mekanik
    E = 0.5 * m * v**2 + V

    # Menyimpan data
    waktu.append(t * 1e15)       # fs
    posisi.append(x * 1e9)       # nm
    kecepatan.append(v)
    energi.append(E)

    # Percepatan partikel
    a = F / m

    # Metode Euler: memperbarui posisi dan kecepatan
    x_baru = x + v * dt
    v_baru = v + a * dt

    x = x_baru
    v = v_baru

# Menampilkan beberapa hasil
print("Simulasi Sumur Potensial Berhingga")
print(f"{'Waktu (fs)':<15}{'Posisi (nm)':<18}"
      f"{'Kecepatan (m/s)':<22}{'Energi (J)':<18}")

for i in range(0, len(waktu), max(1, jumlah // 10)):
    print(f"{waktu[i]:<15.3f}{posisi[i]:<18.6f}"
          f"{kecepatan[i]:<22.4f}{energi[i]:<18.4e}")

# Grafik posisi terhadap waktu
plt.figure()
plt.plot(waktu, posisi)
plt.xlabel("Waktu (fs)")
plt.ylabel("Posisi partikel (nm)")
plt.title("Gerak Partikel dalam Sumur Potensial")
plt.grid(True)
plt.show()

# Grafik energi mekanik terhadap waktu
plt.figure()
plt.plot(waktu, energi)
plt.xlabel("Waktu (fs)")
plt.ylabel("Energi mekanik (J)")
plt.title("Energi Mekanik Partikel")
plt.grid(True)
plt.show()
