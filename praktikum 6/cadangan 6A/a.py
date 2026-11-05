
# TURUNAN PERTAMA METODE BEDA TENGAH DUA TITIK

# Membaca fungsi dan nilai x
fungsi = input("Masukkan fungsi f(x): ")
x = float(input("Masukkan nilai x: "))
e = float(input("Masukkan toleransi error: "))

# Nilai awal sesuai flowchart
h = 1.0
n = 0
z = 0.0
d = 0.0

# Menghitung turunan pertama
while True:

    # Menghitung f(x+h) dan f(x-h)
    x1 = x + h
    x2 = x - h

    f1 = eval(fungsi, {"x": x1})
    f2 = eval(fungsi, {"x": x2})

    # Beda tengah dua titik
    dx = (f1 - f2) / (2 * h)

    # Menghitung selisih hasil turunan
    d = z - dx

    # Menampilkan hasil iterasi
    n = n + 1
    print("Iterasi =", n)
    print("h       =", h)
    print("Turunan =", dx)
    print("Error   =", abs(d))
    print()

    # Memeriksa toleransi error
    if n > 1 and abs(d) <= e:
        break

    # Memperbarui nilai
    z = dx
    h = h / 10
# Menampilkan hasil akhir
print("Turunan pertama f'(", x, ") =", dx)
