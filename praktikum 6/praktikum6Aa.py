# TURUNAN PERTAMA METODE BEDA TENGAH DUA TITIK

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

    # Menghitung turunan pertama
    x1 = x + h
    x2 = x - h

    z1 = eval(fungsi, {"x": x1})
    z2 = eval(fungsi, {"x": x2})

    dx = (z1 - z2) / (2 * h)

    d = abs((h**2 / 6) * d3)

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

print("Turunan pertama f'(", x, ") =", dx)
print("Error akhir =", d)