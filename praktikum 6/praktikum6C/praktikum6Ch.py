
# SIMULASI POSISI DAN KECEPATAN PLANET
# METODE NUMERIK TURUNAN KEDUA (BEDA TENGAH)

# Konstanta gravitasi dan massa Matahari
G = 6.6743e-11
Ms = 1.989e30
ME = 5.972e24

# Posisi awal planet
x0 = float(input("Masukkan posisi awal x (m) : "))
y0 = float(input("Masukkan posisi awal y (m) : "))

# Kecepatan awal planet
vx0 = float(input("Masukkan kecepatan awal vx (m/s) : "))
vy0 = float(input("Masukkan kecepatan awal vy (m/s) : "))

# Langkah waktu dan waktu maksimum
dt = float(input("Masukkan langkah waktu dt (s) : "))
tmaks = float(input("Masukkan waktu maksimum (s) : "))

# Inisialisasi waktu dan posisi
t = 0
n = 0

# Menghitung posisi pada langkah pertama
r0 = (x0**2 + y0**2)**0.5

ax0 = -G * Ms * x0 / r0**3
ay0 = -G * Ms * y0 / r0**3

x1 = x0 + vx0 * dt + 0.5 * ax0 * dt**2
y1 = y0 + vy0 * dt + 0.5 * ay0 * dt**2

# Posisi sebelumnya dan posisi sekarang
xp = x0
yp = y0
x = x1
y = y1

print("\nHASIL PERHITUNGAN")
print("-" * 90)
print(f"{'n':<6}{'Waktu (s)':<18}{'Posisi x (m)':<22}{'Posisi y (m)':<22}{'Vx (m/s)':<15}{'Vy (m/s)':<15}")

while t < tmaks:

    # Menghitung jarak planet
    r = (x**2 + y**2)**0.5

    # Menghitung percepatan
    ax = -G * Ms * x / r**3
    ay = -G * Ms * y / r**3

    # Menghitung posisi berikutnya dengan beda tengah
    xn = 2 * x - xp + ax * dt**2
    yn = 2 * y - yp + ay * dt**2

    # Menghitung kecepatan dengan beda tengah
    vx = (xn - xp) / (2 * dt)
    vy = (yn - yp) / (2 * dt)

    # Memperbarui waktu
    t = t + dt
    n = n + 1

    # Menampilkan hasil
    print(f"{n:<6}{t:<18.2f}{xn:<22.3f}{yn:<22.3f}{vx:<15.3f}{vy:<15.3f}")

    # Memperbarui posisi
    xp = x
    yp = y
    x = xn
    y = yn

print("-" * 90)
print("Perhitungan selesai.")
