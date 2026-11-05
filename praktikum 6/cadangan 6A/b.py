
# TURUNAN PERTAMA METODE BEDA TENGAH EMPAT TITIK

# Baca nilai fungsi
fungsi = input("Masukkan fungsi f(x): ")
x = float(input("Masukkan nilai x: "))
e = float(input("Masukkan toleransi error: "))

# Inisialisasi
h = 1.0
n = 0
d = 0.0

while True:
    n = n + 1

    # Menghitung turunan pertama
    f1 = eval(fungsi, {"x": x - 2*h})
    f2 = eval(fungsi, {"x": x - h})
    f3 = eval(fungsi, {"x": x + h})
    f4 = eval(fungsi, {"x": x + 2*h})

    dx = (f1 - 8*f2 + 8*f3 - f4) / (12*h)

    # Menghitung turunan kelima secara numerik
    f1 = eval(fungsi, {"x": x - 3*h})
    f2 = eval(fungsi, {"x": x - 2*h})
    f3 = eval(fungsi, {"x": x - h})
    f4 = eval(fungsi, {"x": x})
    f5 = eval(fungsi, {"x": x + h})
    f6 = eval(fungsi, {"x": x + 2*h})
    f7 = eval(fungsi, {"x": x + 3*h})

    d5 = (f1 - 5*f2 + 10*f3 - 10*f5
          + 5*f6 - f7) / (2*h**5)

    # Menghitung error sisa Taylor
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

    if n >= 15:
        break

print("Turunan pertama f'(", x, ") =", dx)
print("Error akhir =", d)
