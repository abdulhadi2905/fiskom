
# TURUNAN PERTAMA METODE BEDA DEPAN EMPAT TITIK

# Baca nilai fungsi
fungsi = input("Masukkan fungsi f(x): ")
x = float(input("Masukkan nilai x: "))
e = float(input("Masukkan toleransi error: "))
d4 = float(input("Masukkan turunan keempat f''''(x): "))

# Inisialisasi
h = 1.0
n = 0
z = 0.0
d = 0.0

while True:
    n = n + 1

    # Menghitung turunan pertama
    x1 = x + h
    x2 = x + 2*h
    x3 = x + 3*h

    z1 = eval(fungsi, {"x": x})
    z2 = eval(fungsi, {"x": x1})
    z3 = eval(fungsi, {"x": x2})
    z4 = eval(fungsi, {"x": x3})

    dx = (-11*z1 + 18*z2 - 9*z3 + 2*z4) / (6*h)

    # Menghitung error sisa deret Taylor
    d = abs((h**3 / 4) * d4)

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
