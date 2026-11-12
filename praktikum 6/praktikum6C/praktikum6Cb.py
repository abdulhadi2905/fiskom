
# TURUNAN KEDUA FUNGSI DUA DIMENSI
# METODE BEDA TENGAH 5 TITIK

# Baca fungsi dan nilai awal
fungsi = input("Masukkan fungsi f(x,y): ")
x = float(input("Masukkan nilai x: "))
y = float(input("Masukkan nilai y: "))
h = float(input("Masukkan ukuran langkah awal (h): "))
e = float(input("Masukkan toleransi error: "))

# Definisi fungsi
def f(X, Y):
    return eval(fungsi, {"__builtins__": {}}, {"x": X, "y": Y})

# Inisialisasi
n = 0
ex = 0
ey = 0

while True:

    # Turunan kedua terhadap x dengan langkah h
    fxx1 = (-f(x+2*h,y) + 16*f(x+h,y)
            - 30*f(x,y) + 16*f(x-h,y)
            - f(x-2*h,y)) / (12*h**2)

    # Turunan kedua terhadap y dengan langkah h
    fyy1 = (-f(x,y+2*h) + 16*f(x,y+h)
            - 30*f(x,y) + 16*f(x,y-h)
            - f(x,y-2*h)) / (12*h**2)

    # Ukuran langkah baru
    hh = h / 2

    # Turunan kedua terhadap x dengan langkah hh
    fxx2 = (-f(x+2*hh,y) + 16*f(x+hh,y)
            - 30*f(x,y) + 16*f(x-hh,y)
            - f(x-2*hh,y)) / (12*hh**2)

    # Turunan kedua terhadap y dengan langkah hh
    fyy2 = (-f(x,y+2*hh) + 16*f(x,y+hh)
            - 30*f(x,y) + 16*f(x,y-hh)
            - f(x,y-2*hh)) / (12*hh**2)

    # Menghitung error
    ex = abs(fxx2 - fxx1) / 15
    ey = abs(fyy2 - fyy1) / 15

    # Pemeriksaan toleransi error
    if ex <= e and ey <= e:
        break

    # Memperkecil ukuran langkah
    h = h / 2
    n = n + 1

    if n >= 50:
        break

# Menampilkan hasil
print("\nHASIL PERHITUNGAN")
print("-----------------------------------")
print("Turunan kedua terhadap x =", fxx2)
print("Turunan kedua terhadap y =", fyy2)
print("Error turunan x          =", ex)
print("Error turunan y          =", ey)
print("Ukuran langkah           =", hh)
print("Jumlah iterasi           =", n)

if ex <= e and ey <= e:
    print("Keterangan: Toleransi error terpenuhi")
else:
    print("Keterangan: Toleransi error belum terpenuhi")
