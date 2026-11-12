
# MENGHITUNG LAJU ALIRAN KALOR PADA BATANG
# METODE NUMERIK TURUNAN BEDA TENGAH

# Memasukkan persamaan temperatur
T = input("Masukkan persamaan temperatur T(x) : ")
f = eval("lambda x: " + T)

# Memasukkan nilai
x = float(input("Masukkan posisi x : "))
h = float(input("Masukkan langkah ruang h : "))
k = float(input("Masukkan konduktivitas termal k : "))
A = float(input("Masukkan luas penampang batang A : "))

# Menghitung temperatur pada x+h dan x-h
T1 = f(x+h)
T2 = f(x-h)

# Menghitung turunan pertama dengan beda tengah
dT = (T1-T2)/(2*h)

# Menghitung laju aliran kalor
Q = -k*A*dT

# Menampilkan hasil
print("\nHASIL PERHITUNGAN")
print("Temperatur T(x+h) =", T1)
print("Temperatur T(x-h) =", T2)
print("Turunan suhu      =", dT)
print("Laju aliran kalor =", Q)
