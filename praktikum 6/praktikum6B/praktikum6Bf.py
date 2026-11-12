
# MENGHITUNG KECEPATAN DAN PERCEPATAN GERAK PELURU
# METODE BEDA MAJU

# Input data
v0 = float(input("Masukkan kecepatan awal (m/s): "))
sudut = float(input("Masukkan sudut elevasi (derajat): "))
dt = float(input("Masukkan selang waktu (delta t): "))
tmax = float(input("Masukkan waktu akhir simulasi: "))

# Konstanta gravitasi
g = 9.8

# Konversi sudut derajat ke radian
x = sudut * 3.141592653589793 / 180

# Menghitung cosinus menggunakan deret Taylor
cosx = 1
z = -x**2
suku = 1

for n in range(1, 16):
    suku = suku * z / ((2*n-1)*(2*n))
    cosx = cosx + suku

# Menghitung sinus menggunakan deret Taylor
sinx = x
z = -x**2
suku = x

for n in range(1, 16):
    suku = suku * z / ((2*n)*(2*n+1))
    sinx = sinx + suku

# Inisialisasi waktu
t = 0
n = 0

print("\nHASIL SIMULASI GERAK PELURU")
print("---------------------------------------------------------------")
print(f"{'N':<5}{'Waktu':<10}{'Vx':<12}{'Vy':<12}{'V':<12}{'Ax':<12}{'Ay':<12}{'A':<12}")

while t <= tmax:

    # Menghitung posisi pada waktu t
    sx0 = v0 * cosx * t
    sy0 = v0 * sinx * t - 0.5 * g * t**2

    # Menghitung posisi pada waktu t + dt
    sx1 = v0 * cosx * (t + dt)
    sy1 = v0 * sinx * (t + dt) - 0.5 * g * (t + dt)**2

    # Menghitung posisi pada waktu t + 2dt
    sx2 = v0 * cosx * (t + 2*dt)
    sy2 = v0 * sinx * (t + 2*dt) - 0.5 * g * (t + 2*dt)**2

    # Menghitung kecepatan metode beda maju
    vx = (sx1 - sx0) / dt
    vy = (sy1 - sy0) / dt

    # Menghitung percepatan metode beda maju
    ax = (sx2 - 2*sx1 + sx0) / dt**2
    ay = (sy2 - 2*sy1 + sy0) / dt**2

    # Menghitung besar kecepatan
    v = (vx**2 + vy**2)**0.5

    # Menghitung besar percepatan
    a = (ax**2 + ay**2)**0.5

    # Menampilkan hasil
    print(f"{n:<5}{t:<10.3f}{vx:<12.5f}{vy:<12.5f}{v:<12.5f}{ax:<12.5f}{ay:<12.5f}{a:<12.5f}")

    # Menambah waktu dan iterasi
    t = t + dt
    n = n + 1

print("---------------------------------------------------------------")
print("Simulasi selesai")
