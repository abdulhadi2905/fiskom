
# SIMULASI GERAK PENDULUM DENGAN REDAMAN
# METODE EULER

# Baca nilai awal
L = float(input("Masukkan panjang tali (m): "))
m = float(input("Masukkan massa pendulum (kg): "))
theta = float(input("Masukkan sudut awal (radian): "))
omega = float(input("Masukkan kecepatan sudut awal (rad/s): "))
q = float(input("Masukkan parameter redaman (q): "))

g = 9.8

dt = float(input("Masukkan selang waktu (dt): "))
tmaks = float(input("Masukkan waktu maksimum (s): "))

# Inisialisasi
t = 0
n = 0

# Menampilkan judul tabel
print("\nSIMULASI PENDULUM DENGAN REDAMAN")
print("---------------------------------------------------")
print("Waktu(s)   Sudut(rad)   Kecepatan(rad/s)   Posisi(m)")
print("---------------------------------------------------")

# Perulangan perhitungan
while t <= tmaks:

    # Menghitung posisi busur
    s = L * theta

    # Menampilkan hasil
    print(f"{t:8.3f} {theta:12.6f} {omega:18.6f} {s:12.6f}")

    # Menghitung percepatan sudut
    alpha = -(g/L)*theta - (q/(m*L))*omega

    # Menghitung kecepatan sudut berikutnya
    omega_baru = omega + alpha*dt

    # Menghitung sudut berikutnya
    theta_baru = theta + omega*dt

    # Memperbarui nilai
    theta = theta_baru
    omega = omega_baru

    # Memperbarui waktu
    t = t + dt
    n = n + 1

    if n >= 100000:
        break

print("---------------------------------------------------")
print("Jumlah iterasi =", n)
print("Simulasi selesai")
