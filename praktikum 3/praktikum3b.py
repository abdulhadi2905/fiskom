
# METODE INVERSI MODEL PARABOLA

# a. Input jumlah seluruh data
n = int(input("Jumlah data (n) : "))

# b. Input data z dan z^2 dalam matriks G
G = []

for i in range(n):
    z = float(input(f"Masukkan kedalaman z{i+1} : "))
    G.append([1.0, z, z**2])

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

# f. Menghitung jumlah yang diperlukan
jumlah_z = 0.0
jumlah_z2 = 0.0
jumlah_z3 = 0.0
jumlah_z4 = 0.0
jumlah_T = 0.0
jumlah_zT = 0.0
jumlah_z2T = 0.0

for i in range(n):
    z = G[i][1]
    T = d[i][0]

    jumlah_z = jumlah_z + z
    jumlah_z2 = jumlah_z2 + z**2
    jumlah_z3 = jumlah_z3 + z**3
    jumlah_z4 = jumlah_z4 + z**4
    jumlah_T = jumlah_T + T
    jumlah_zT = jumlah_zT + z*T
    jumlah_z2T = jumlah_z2T + z**2*T

print("\nJumlah perhitungan:")
print("Jumlah z       =", jumlah_z)
print("Jumlah z^2     =", jumlah_z2)
print("Jumlah z^3     =", jumlah_z3)
print("Jumlah z^4     =", jumlah_z4)
print("Jumlah T       =", jumlah_T)
print("Jumlah z*T     =", jumlah_zT)
print("Jumlah z^2*T   =", jumlah_z2T)

# g. Membuat transpose G dan matriks GG = GTG
GT = []

for j in range(3):
    baris = []
    for i in range(n):
        baris.append(G[i][j])
    GT.append(baris)

GG = [[0.0 for j in range(3)] for i in range(3)]

for i in range(3):
    for j in range(3):
        for k in range(n):
            GG[i][j] = GG[i][j] + GT[i][k] * G[k][j]

print("\nMatriks GG = GTG:")
for baris in GG:
    print(baris)

# h. Membuat matriks Gd = GTd
Gd = [[0.0] for i in range(3)]

for i in range(3):
    for k in range(n):
        Gd[i][0] = Gd[i][0] + GT[i][k] * d[k][0]

print("\nMatriks Gd = GTd:")
for baris in Gd:
    print(baris)

# i. Membuat invers matriks GG dengan eliminasi Gauss-Jordan
A = []

for i in range(3):
    baris = []

    for j in range(3):
        baris.append(GG[i][j])

    for j in range(3):
        if i == j:
            baris.append(1.0)
        else:
            baris.append(0.0)

    A.append(baris)

singular = False

for i in range(3):

    # Mencari baris dengan nilai pivot terbesar
    pivot_baris = i

    for k in range(i + 1, 3):
        if abs(A[k][i]) > abs(A[pivot_baris][i]):
            pivot_baris = k

    if abs(A[pivot_baris][i]) < 1e-12:
        singular = True
        break

    # Menukar baris jika diperlukan
    A[i], A[pivot_baris] = A[pivot_baris], A[i]

    # Membuat elemen pivot menjadi 1
    pivot = A[i][i]

    for j in range(6):
        A[i][j] = A[i][j] / pivot

    # Membuat elemen lain pada kolom pivot menjadi 0
    for k in range(3):
        if k != i:
            faktor = A[k][i]

            for j in range(6):
                A[k][j] = A[k][j] - faktor * A[i][j]

if singular:
    print("\nMatriks GG tidak memiliki invers.")
else:
    invG = []

    for i in range(3):
        baris = []

        for j in range(3, 6):
            baris.append(A[i][j])

        invG.append(baris)

    print("\nMatriks invers invG:")
    for baris in invG:
        print(baris)

    # j. Menghitung m = invG * Gd
    m = [[0.0] for i in range(3)]

    for i in range(3):
        for j in range(3):
            m[i][0] = m[i][0] + invG[i][j] * Gd[j][0]

    # k. Cetak matriks m
    print("\nMatriks m:")
    for baris in m:
        print(baris)

    # l. Cetak parameter m1, m2, dan m3
    m1 = m[0][0]
    m2 = m[1][0]
    m3 = m[2][0]

    print("\nNilai parameter:")
    print("m1 =", m1)
    print("m2 =", m2)
    print("m3 =", m3)

    # m. Cetak persamaan model parabola
    print("\nPersamaan model matematis:")
    print(f"T(z) = {m1} + ({m2})z + ({m3})z^2")
