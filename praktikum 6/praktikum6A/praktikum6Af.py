
# TURUNAN PERTAMA DAN KEDUA METODE BEDA TENGAH

# Baca nilai fungsi
fungsi = input("Masukkan fungsi f(x): ")
x = float(input("Masukkan nilai x: "))
h = float(input("Masukkan langkah ruang h: "))

# Menghitung nilai fungsi
x1 = x + h
x2 = x
x3 = x - h

f1 = eval(fungsi, {"x": x1})
f2 = eval(fungsi, {"x": x2})
f3 = eval(fungsi, {"x": x3})

# Menghitung turunan pertama
d1 = (f1 - f3) / (2 * h)

# Menghitung turunan kedua
d2 = (f1 - (2 * f2) + f3) / (h ** 2)

# Menampilkan hasil
print("\nHASIL PERHITUNGAN")
print("f(x+h) =", f1)
print("f(x)   =", f2)
print("f(x-h) =", f3)

print("\nTurunan pertama f'(x) =", d1)
print("Turunan kedua f''(x)  =", d2)
