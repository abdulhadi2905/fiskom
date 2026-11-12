
# TURUNAN PERTAMA FUNGSI DUA DIMENSI
# METODE BEDA TENGAH 5 TITIK

# Input data
fungsi = input("Masukkan fungsi f(x,y): ")
x = float(input("Masukkan nilai x: "))
y = float(input("Masukkan nilai y: "))
h = float(input("Masukkan ukuran langkah awal (h): "))
e = float(input("Masukkan toleransi error: "))
d5 = float(input("Masukkan turunan kelima f'''''(x): "))

# Fungsi untuk menghitung nilai f(x,y)
def f(X, Y):
    return eval(fungsi, {"__builtins__": {}}, {"x": X, "y": Y})

# Inisialisasi
n = 0
ex = 0
ey = 0

# Perulangan untuk memperkecil error
while True:

    # Turunan terhadap x dengan langkah h
    fx1 = (f(x-2*h,y) - 8*f(x-h,y) +
           8*f(x+h,y) - f(x+2*h,y)) / (12*h)

    # Turunan terhadap y dengan langkah h
    fy1 = (f(x,y-2*h) - 8*f(x,y-h) +
           8*f(x,y+h) - f(x,y+2*h)) / (12*h)

    ex = abs((h**4/30) * d5)
    ey = abs((h**4/30) * d5)

    # Pemeriksaan error
    if ex <= e and ey <= e:
        break

    # Memperkecil ukuran langkah
    h = h / 2
    n = n + 1

    # Batas iterasi
    if n >= 50:
        break

# Hasil turunan
print("\nHASIL PERHITUNGAN")
print("-----------------------------------")
print("Turunan terhadap x =", fx1)
print("Turunan terhadap y =", fy1)
print("Error turunan x    =", ex)
print("Error turunan y    =", ey)
print("Ukuran langkah     =", h)
print("Jumlah iterasi     =", n)

if ex <= e and ey <= e:
    print("Keterangan: Toleransi error terpenuhi")
else:
    print("Keterangan: Toleransi error belum terpenuhi")
