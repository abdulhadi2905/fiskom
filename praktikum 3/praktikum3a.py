
# METODE INVERSI MODEL GARIS

# a. Input jumlah seluruh data
n = int(input("Jumlah data (n) : "))

# b. Input data kedalaman dalam matriks G
G = []

for i in range(n):
    z = float(input(f"Masukkan kedalaman z{i+1} : "))
    G.append([1.0, z])

# c. Cetak matriks G
print("\nMatriks G:")
for baris in G:
    print(baris)

# d. Input data temperatur dalam matriks d
d = []

for j in range(n):
    T = float(input(f"Masukkan temperatur T{j+1} : "))
    d.append([T])

# e. Cetak matriks d
print("\nMatriks d:")
for baris in d:
    print(baris)

# f. Hitung jumlah data
jumlah_z = 0.0
jumlah_z2 = 0.0
jumlah_T = 0.0
jumlah_zT = 0.0

for i in range(n):
    z = G[i][1]
    T = d[i][0]

    jumlah_z = jumlah_z + z
    jumlah_z2 = jumlah_z2 + z**2
    jumlah_T = jumlah_T + T
    jumlah_zT = jumlah_zT + z*T

print("\nJumlah perhitungan:")
print("Jumlah z       =", jumlah_z)
print("Jumlah z^2     =", jumlah_z2)
print("Jumlah T       =", jumlah_T)
print("Jumlah z*T     =", jumlah_zT)

# g. Membuat matriks GT dan GG = GTG
GT = []

for j in range(2):
    baris = []

    for i in range(n):
        baris.append(G[i][j])

    GT.append(baris)

GG = [[0.0, 0.0],
      [0.0, 0.0]]

for i in range(2):
    for j in range(2):
        for k in range(n):
            GG[i][j] = GG[i][j] + GT[i][k] * G[k][j]

print("\nMatriks GG = GTG:")
for baris in GG:
    print(baris)

# h. Membuat matriks Gd = GTd
Gd = [[0.0],
      [0.0]]

for i in range(2):
    for k in range(n):
        Gd[i][0] = Gd[i][0] + GT[i][k] * d[k][0]

print("\nMatriks Gd = GTd:")
for baris in Gd:
    print(baris)

# i. Membuat invers matriks GG
a = GG[0][0]
b = GG[0][1]
c = GG[1][0]
e = GG[1][1]

det = a*e - b*c

print("\nDeterminan GG =", det)

if det == 0:
    print("Matriks GG tidak memiliki invers.")

else:
    invG = [
        [e/det, -b/det],
        [-c/det, a/det]
    ]

    print("\nMatriks invers invG:")
    for baris in invG:
        print(baris)

    # j. Menghitung m = invG * Gd
    m = [[0.0],
         [0.0]]

    for i in range(2):
        for k in range(2):
            m[i][0] = m[i][0] + invG[i][k] * Gd[k][0]

    # k. Cetak matriks m
    print("\nMatriks m:")
    for baris in m:
        print(baris)

    # l. Cetak nilai m1 dan m2
    m1 = m[0][0]
    m2 = m[1][0]

    print("\nNilai parameter:")
    print("m1 =", m1)
    print("m2 =", m2)

    # m. Cetak persamaan model matematis
    print("\nPersamaan model matematis:")
    print(f"T(z) = {m1} + ({m2})z")
