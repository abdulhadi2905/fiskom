from math import sin, cos, tan, exp
# MENGHITUNG GRADIEN SUHU DAN KONDUKTIVITAS TERMAL
# METODE NUMERIK TURUNAN BEDA TENGAH

# Memasukkan persamaan suhu
T = input("Masukkan persamaan suhu T(x,y) : ")
f = eval("lambda x,y: " + T)

# Memasukkan titik yang akan dihitung
x = float(input("Masukkan nilai x : "))
y = float(input("Masukkan nilai y : "))

# Memasukkan langkah ruang
h = float(input("Masukkan langkah ruang h : "))

# Memasukkan aliran panas
Q = float(input("Masukkan aliran panas Q : "))

# Luas permukaan sampel
A = 3 * 5

# Menghitung turunan parsial terhadap x
Tx = (f(x+h,y) - f(x-h,y)) / (2*h)

# Menghitung turunan parsial terhadap y
Ty = (f(x,y+h) - f(x,y-h)) / (2*h)

# Menghitung besar gradien suhu
grad = (Tx**2 + Ty**2)**0.5

# Menghitung konduktivitas termal
k = Q / (A * grad)

# Menampilkan hasil
print("\nHASIL PERHITUNGAN")
print("Turunan suhu terhadap x =", Tx)
print("Turunan suhu terhadap y =", Ty)
print("Gradien suhu             =", grad)
print("Luas sampel              =", A)
print("Konduktivitas termal k   =", k)
