# TURUNAN KEDUA METODE BEDA BELAKANG 3 TITIK

# Baca nilai fungsi
fungsi = input("Masukkan fungsi f(x): ")
x = float(input("Masukkan nilai x: "))
e = float(input("Masukkan toleransi error: "))
d3 = float(input("Masukkan turunan ketiga f'''(x): "))

# Inisialisasi
h = 1.0
n = 0
z = 0.0
d = 0.0

while True:
    n = n + 1

    # Menghitung turunan kedua
    x1 = x
    x2 = x - h
    x3 = x - 2*h

    z1 = eval(fungsi, {"x": x1})
    z2 = eval(fungsi, {"x": x2})
    z3 = eval(fungsi, {"x": x3})

    # Turunan kedua beda belakang 3 titik
    dx = (z3 - 2*z2 + z1) / (h**2)

    d = abs(h * d3)

    print("Iterasi =", n)
    print("h       =", h)
    print("Turunan =", dx)
    print("Error   =", d)
    print()

    # Pengujian toleransi error
    if d <= e:
        break

    # Memperbarui nilai h
    h = h / 10

print("Turunan kedua f''(", x, ") =", dx)
print("Error akhir =", d)