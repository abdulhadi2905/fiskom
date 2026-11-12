
# TURUNAN PERTAMA METODE BEDA HINGGA

# Data tabel
x = [1.33, 1.5, 1.7, 1.9, 2.1, 2.3, 2.5]
f = [3.669, 4.482, 5.474, 6.686, 8.166, 9.974, 12.182]

# Fungsi menghitung turunan pertama
def turunan(x0, titik):
    hasil = 0.0

    for i in range(len(titik)):
        xi = titik[i]
        pembagi = 1.0

        for j in range(len(titik)):
            if i != j:
                pembagi = pembagi * (xi - titik[j])

        bobot = 0.0

        for m in range(len(titik)):
            if m != i:
                perkalian = 1.0

                for j in range(len(titik)):
                    if j != i and j != m:
                        perkalian = perkalian * (x0 - titik[j])

                bobot = bobot + perkalian / pembagi

        # Mencari nilai fungsi sesuai titik
        k = x.index(xi)
        hasil = hasil + bobot * f[k]

    return hasil


# 1. Turunan di x = 1.7
titik_1 = [1.5, 1.7, 1.9]
titik_2 = [1.33, 1.5, 1.7, 1.9, 2.1]

d1 = turunan(1.7, titik_1)
d2 = turunan(1.7, titik_2)

# 2. Turunan di x = 1.4
titik_3 = [1.33, 1.5, 1.7]
d3 = turunan(1.4, titik_3)

# 3. Turunan di x = 1.3 dan x = 2.5
titik_4 = [1.33, 1.5, 1.7]
titik_5 = [2.1, 2.3, 2.5]

d4 = turunan(1.3, titik_4)
d5 = turunan(2.5, titik_5)

# Menampilkan hasil
print("HASIL PERHITUNGAN TURUNAN PERTAMA")
print("-----------------------------------")
print("1. f'(1.7) orde O(h^2) =", d1)
print("2. f'(1.7) orde O(h^4) =", d2)
print("3. f'(1.4) orde O(h^2) =", d3)
print("4. f'(1.3) =", d4)
print("5. f'(2.5) =", d5)
