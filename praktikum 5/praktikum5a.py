
# METODE NEWTON-RAPHSON STANDAR

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

    # fx = f(x) = x^2 - 2x - 8
    fx = x**2 - 2*x - 8

    # dx = f'(x) = 2x - 2
    dx = 2*x - 2

    # Memeriksa turunan agar tidak dibagi nol
    if dx == 0:
        dx += 0.01  # Menambahkan nilai kecil untuk menghindari pembagian nol

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
