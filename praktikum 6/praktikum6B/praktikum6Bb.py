
# TURUNAN PERTAMA DAN KEDUA METODE BEDA TENGAH

# Data pengukuran
x = [0, 1, 2, 3, 4, 5, 6]
y = [6.9897, 7.4036, 7.7814, 8.1291,
     8.4410, 8.7406, 9.0309]

# Inisialisasi
h = 1.0
titik = [1, 3, 5]

# Perhitungan turunan
print("HASIL PERHITUNGAN TURUNAN")
print("--------------------------------")

for a in titik:

    # Menentukan indeks titik x
    i = x.index(a)

    # Menghitung turunan pertama
    dy = (y[i+1] - y[i-1]) / (2*h)

    # Menghitung turunan kedua
    d2y = (y[i+1] - 2*y[i] + y[i-1]) / (h**2)

    # Menampilkan hasil
    print("\nPada x =", a)
    print("Turunan pertama  =", dy)
    print("Turunan kedua    =", d2y)
