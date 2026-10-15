
# METODE INVERSI MODEL BIDANG

# a. Input jumlah seluruh data
n = int(input("Jumlah data (n) : "))

# b. Input data x dan y dalam matriks G
G = []

for i in range(n):
    x = float(input(f"Masukkan nilai x{i+1} : "))
    y = float(input(f"Masukkan nilai y{i+1} : "))
    G.append([1.0, x, y])

# c. Cetak matriks G
print("\nMatriks G:")
for baris in G:
    print(baris)

# d. Input data d dalam matriks d
d = []

for j in range(n):
    nilai = float(input(f"Masukkan nilai d{j+1} : "))
    d.append([nilai])

# e. Cetak matriks d
print("\nMatriks d:")
for baris in d:
    print(baris)

# f. Menghitung jumlah yang diperlukan
jumlah_x = 0.0
jumlah_x2 = 0.0
jumlah_y = 0.0
jumlah_y2 = 0.0
jumlah_xy = 0.0
jumlah_d = 0.0
jumlah_xd = 0.0
jumlah_yd = 0.0

for i in range(n):
    x = G[i][1]
    y = G[i][2]
    nilai = d[i][0]

    jumlah_x = jumlah_x + x
    jumlah_x2 = jumlah_x2 + x**2
    jumlah_y = jumlah_y + y
    jumlah_y2 = jumlah_y2 + y**2
    jumlah_xy = jumlah_xy + x*y
    jumlah_d = jumlah_d + nilai
    jumlah_xd = jumlah_xd + x*nilai
    jumlah_yd = jumlah_yd + y*nilai

print("\nJumlah perhitungan:")
print("Jumlah x   =", jumlah_x)
print("Jumlah x^2 =", jumlah_x2)
print("Jumlah y   =", jumlah_y)
print("Jumlah y^2 =", jumlah_y2)
print("Jumlah xy  =", jumlah_xy)
print("Jumlah d   =", jumlah_d)
print("Jumlah xd  =", jumlah_xd)
print("Jumlah yd  =", jumlah_yd)

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

    # l. Cetak nilai m1, m2, dan m3
    m1 = m[0][0]
    m2 = m[1][0]
    m3 = m[2][0]

    print("\nNilai parameter:")
    print("m1 =", m1)
    print("m2 =", m2)
    print("m3 =", m3)

    # m. Cetak persamaan model bidang
    print("\nPersamaan model matematis:")
    print(f"d = {m1} + ({m2})x + ({m3})y")
