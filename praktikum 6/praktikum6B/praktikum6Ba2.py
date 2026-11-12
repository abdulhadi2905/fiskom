# TURUNAN KEDUA METODE BEDA BELAKANG
# 3 TITIK DAN 4 TITIK
from math import *

# Baca nilai fungsi
fungsi = input("Masukkan fungsi f(x): ").replace("^", "**")
x = float(input("Masukkan nilai x: "))
e = float(input("Masukkan toleransi error: "))
t3 = float(input("Masukkan turunan ketiga f'''(x): "))
t4 = float(input("Masukkan turunan keempat f''''(x): "))

# Inisialisasi
h = 1.0
n = 0
d = 0.0
d3 = 0.0
d4 = 0.0

while True:
    n = n + 1

    # Menghitung nilai turunan kedua
    x1 = x
    x2 = x - h
    x3 = x - 2*h
    x4 = x - 3*h

    f1 = eval(fungsi, globals(), {"x": x1})
    f2 = eval(fungsi, globals(), {"x": x2})
    f3 = eval(fungsi, globals(), {"x": x3})
    f4 = eval(fungsi, globals(), {"x": x4})

    # Turunan kedua beda belakang 3 titik
    d23 = (f1 - 2*f2 + f3) / (h**2)

    # Turunan kedua beda belakang 4 titik
    d24 = (2*f1 - 5*f2 + 4*f3 - f4) / (h**2)

    # Error masing-masing metode
    d3 = abs(h * t3)               # 3 titik: O(h)
    d4 = abs((11/12) * h**2 * t4)  # 4 titik: O(h^2)
    d = max(d3, d4)

    print("Iterasi        =", n)
    print("h              =", h)
    print("Turunan 3 titik =", d23)
    print("Error 3 titik   =", d3)
    print("Turunan 4 titik =", d24)
    print("Error 4 titik   =", d4)
    print()

    # Pengujian toleransi error (kedua metode harus memenuhi)
    if d <= e:
        break

    # Memperbarui nilai h
    h = h / 10

    if n >= 15:
        print("Peringatan: iterasi maksimum tercapai, toleransi belum terpenuhi.")
        break

print("Turunan kedua 3 titik f''(", x, ") =", d23, " error =", d3)
print("Turunan kedua 4 titik f''(", x, ") =", d24, " error =", d4)