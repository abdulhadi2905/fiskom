# TURUNAN PERTAMA METODE BEDA TENGAH EMPAT TITIK

# Baca nilai fungsi
fungsi = input("Masukkan fungsi f(x): ")
x = float(input("Masukkan nilai x: "))
e = float(input("Masukkan toleransi error: "))
d5 = float(input("Masukkan turunan kelima f'''''(x): "))

# Inisialisasi
h = 1.0
n = 0
z = 0.0
d = 0.0

while True:
    n = n + 1

    # Menghitung turunan pertama
    f1 = eval(fungsi, {"x": x - 2*h})
    f2 = eval(fungsi, {"x": x - h})
    f3 = eval(fungsi, {"x": x + h})
    f4 = eval(fungsi, {"x": x + 2*h})

    dx = (f1 - 8*f2 + 8*f3 - f4) / (12*h)

    d = abs((h**4 / 30) * d5)

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