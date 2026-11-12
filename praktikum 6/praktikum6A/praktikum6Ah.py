
# MENGHITUNG TEGANGAN GESER FLUIDA
# METODE TURUNAN 3 TITIK DAN 4 TITIK

# Data pengukuran
y = [0.0, 0.2, 0.4, 0.6, 0.8]
u = [0.0, 0.0618, 0.1176, 0.1618, 0.1902]

# Nilai yang diketahui
h = 0.2
mu = 0.001

# Menghitung turunan dengan 3 titik
du3 = (-3*u[1] + 4*u[2] - u[3]) / (2*h)

# Menghitung turunan dengan 4 titik
du4 = (-11*u[1] + 18*u[2] - 9*u[3] + 2*u[4]) / (6*h)

# Menghitung tegangan geser
tau3 = mu * du3
tau4 = mu * du4

# Menampilkan hasil
print("HASIL PERHITUNGAN TEGANGAN GESER")
print("----------------------------------")

print("Kasus 3 titik (i = 2, 3, 4)")
print("Turunan kecepatan =", du3, "1/s")
print("Tegangan geser    =", tau3, "N/m^2")

print()

print("Kasus 4 titik (i = 2, 3, 4, 5)")
print("Turunan kecepatan =", du4, "1/s")
print("Tegangan geser    =", tau4, "N/m^2")
