
# METODE SECANT STANDAR

# Baca dua nilai awal
y = []

y0 = float(input("Masukkan nilai awal y(0) : "))
y1 = float(input("Masukkan nilai awal y(1) : "))

y.append(y0)
y.append(y1)

# Iterasi sebanyak 15 kali
print("\nHasil Iterasi Metode Secant")
print(f"{'N':<10}{'y(n)':<20}{'Error':<20}")

for n in range(1, 16):

    # Mengambil dua nilai pendekatan terakhir
    x0 = y[n-1]
    x1 = y[n]

    # Menghitung nilai fungsi pada kedua pendekatan
    f0 = x0**2 - 2*x0 - 8
    f1 = x1**2 - 2*x1 - 8

    # Memeriksa penyebut agar tidak dibagi nol
    penyebut = f1 - f0

    if penyebut == 0:
        print("Penyebut bernilai nol. Iterasi dihentikan.")
        break

    # Menghitung perkiraan akar berikutnya
    yn = x1 - (f1 * (x1 - x0)) / penyebut

    # Menghitung error
    Err = abs(yn - x1)

    # Menyimpan hasil iterasi
    y.append(yn)

    # Menampilkan hasil
    print(f"{n:<10}{yn:<20.10f}{Err:<20.10f}")

# Menampilkan akar pendekatan terakhir
print("\nAkar pendekatan =", y[-1])
