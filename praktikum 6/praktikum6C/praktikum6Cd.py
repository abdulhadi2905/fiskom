
# MENGHITUNG LAJU ALIRAN KALOR PADA FLAT
# TITIK (x,y) = (2,2)

# Konduktivitas termal
k = 202

# Data posisi
x = [1.0, 1.5, 2.0, 2.5, 3.0]
y = [1.0, 1.5, 2.0, 2.5, 3.0]

# Data suhu T(x,y)
T = [
    [1.63, 2.05, 2.50, 2.98, 3.49],
    [1.98, 2.51, 3.08, 3.69, 4.33],
    [2.28, 2.91, 3.61, 4.37, 5.17],
    [2.64, 3.25, 4.08, 5.00, 5.98],
    [2.65, 3.50, 4.48, 5.57, 6.76]
]

# Ukuran langkah
h = 0.5

# Titik yang dihitung (x=2, y=2)
i = 2
j = 2

# Turunan suhu terhadap x
dx = (T[j][i+1] - T[j][i-1]) / (2*h)

# Turunan suhu terhadap y
dy = (T[j+1][i] - T[j-1][i]) / (2*h)

# Luas penampang
A = x[i] * y[j]

# Menghitung laju aliran kalor
Q = -k * A * (dx + dy)

# Menampilkan hasil
print("\nHASIL PERHITUNGAN")
print("-----------------------------------")
print("Titik x                 =", x[i])
print("Titik y                 =", y[j])
print("Konduktivitas termal    =", k, "W/m.C")
print("Luas penampang          =", A)
print("Turunan terhadap x      =", dx)
print("Turunan terhadap y      =", dy)
print("Laju aliran kalor       =", Q, "W")
