
# METODE NEWTON-RAPHSON UNTUK f(x) = e^x - 5x^2

import math

# Baca nilai awal
y = []
y1 = float(input("Masukkan nilai awal y(1) : "))
y.append(y1)

# Iterasi sebanyak 15 kali
print("\nHasil Iterasi Newton-Raphson")
print(f"{'N':<10}{'y(n)':<20}{'Error':<20}")

for n in range(1, 16):

    # x = y(n)
    x = y[n-1]

    # fx = f(x) = e^x - 5x^2
    fx = math.exp(x) - 5*x**2

    # dx = f'(x) = e^x - 10x
    dx = math.exp(x) - 10*x

    # Memeriksa turunan agar tidak dibagi nol
    if dx == 0:
        print("Turunan bernilai nol. Iterasi dihentikan.")
        break

    # Menghitung perkiraan akar berikutnya
    yn = x - fx/dx

    # Menghitung error
    Err = abs(yn - x)

    # Menyimpan hasil iterasi
    y.append(yn)

    # Menampilkan hasil
    print(f"{n:<10}{yn:<20.10f}{Err:<20.10f}")

# Menampilkan akar pendekatan terakhir
print("\nAkar pendekatan =", y[-1])
print("Nilai f(akar) =", math.exp(y[-1]) - 5*y[-1]**2)
