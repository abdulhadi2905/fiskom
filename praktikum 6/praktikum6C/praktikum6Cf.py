
# GERAK OSILASI BANDUL HARMONIS
# METODE BEDA TENGAH

# Baca nilai awal
L = float(input("Masukkan panjang tali (m): "))
theta0 = float(input("Masukkan sudut awal (radian): "))
omega0 = float(input("Masukkan kecepatan sudut awal (rad/s): "))
g = 9.8
dt = float(input("Masukkan selang waktu (dt): "))
tmaks = float(input("Masukkan waktu maksimum (s): "))

# Inisialisasi
t = 0
n = 0

# Sudut awal
theta_sebelumnya = theta0

# Menghitung sudut pada langkah pertama
theta_sekarang = (theta0 + omega0*dt
                  - (g/(2*L))*theta0*dt**2)

# Menampilkan judul tabel
print("\nHASIL PERHITUNGAN GERAK BANDUL")
print("------------------------------------------------")
print("Waktu(s)     Sudut(rad)     Posisi busur(m)")
print("------------------------------------------------")

# Menampilkan kondisi awal
s = L * theta_sebelumnya
print(f"{t:8.3f} {theta_sebelumnya:14.6f} {s:17.6f}")

# Perulangan perhitungan
while t < tmaks:

    # Menghitung sudut berikutnya
    theta_baru = (2*theta_sekarang - theta_sebelumnya
                  - (g/L)*theta_sekarang*dt**2)

    # Memperbarui waktu
    t = t + dt
    n = n + 1

    # Menghitung posisi busur
    s = L * theta_baru

    # Menampilkan hasil
    print(f"{t:8.3f} {theta_baru:14.6f} {s:17.6f}")

    # Memperbarui nilai sudut
    theta_sebelumnya = theta_sekarang
    theta_sekarang = theta_baru

    if n >= 100000:
        break

print("------------------------------------------------")
print("Jumlah iterasi =", n)
print("Perhitungan selesai")
