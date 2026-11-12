
# SIMULASI LAJU ALIRAN KALOR PADA BATANG

import math

# Baca nilai masukan
K = float(input("Masukkan konduktivitas termal (K): "))
A = float(input("Masukkan luas penampang (A): "))
x = float(input("Masukkan ketebalan bahan (x): "))

# Menghitung temperatur
T = x * math.exp(-x**2) - math.tan(x)

# Menghitung turunan temperatur
dT = math.exp(-x**2) * (1 - 2*x**2) - (1 / math.cos(x)**2)

# Menghitung laju aliran kalor
Q = -K * A * dT

# Menampilkan hasil
print("\nHASIL SIMULASI")
print("-----------------------------")
print("Temperatur          =", T)
print("Turunan temperatur  =", dT)
print("Laju aliran kalor   =", Q)
