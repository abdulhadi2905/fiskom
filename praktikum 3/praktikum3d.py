
# METODE INVERSI MODEL GERAK VERTIKAL
# Menentukan kecepatan awal (v0) dan gravitasi (g)

# a. Input jumlah data
n = int(input("Jumlah data (n) : "))

# Input ketinggian awal
h0 = float(input("Ketinggian awal (h0) : "))

# b. Input waktu dan ketinggian
t = []
h = []

for i in range(n):
    print(f"\nData ke-{i+1}")
    waktu = float(input("Waktu t (s) : "))
    tinggi = float(input("Ketinggian h (m) : "))

    t.append(waktu)
    h.append(tinggi)

# Membentuk matriks G dan d
G = []
d = []

for i in range(n):
    G.append([t[i], t[i]**2])
    d.append([h[i] - h0])

# c. Cetak matriks G
print("\nMatriks G:")
for baris in G:
    print(baris)

# d. Cetak matriks d
print("\nMatriks d:")
for baris in d:
    print(baris)

# e. Menghitung matriks GTG dan GTd
a = 0.0
b = 0.0
c = 0.0
u = 0.0
v = 0.0

for i in range(n):
    a = a + t[i]**2
    b = b + t[i]**3
    c = c + t[i]**4

    u = u + t[i] * d[i][0]
    v = v + t[i]**2 * d[i][0]

GG = [
    [a, b],
    [b, c]
]

Gd = [
    [u],
    [v]
]

print("\nMatriks GG = GTG:")
for baris in GG:
    print(baris)

print("\nMatriks Gd = GTd:")
for baris in Gd:
    print(baris)

# f. Menghitung invers matriks GG
det = a*c - b*b

print("\nDeterminan GG =", det)

if abs(det) < 1e-12:
    print("Matriks GG tidak memiliki invers.")

else:
    invG = [
        [c/det, -b/det],
        [-b/det, a/det]
    ]

    print("\nMatriks invers invG:")
    for baris in invG:
        print(baris)

    # g. Menghitung m = invG * Gd
    m1 = invG[0][0]*u + invG[0][1]*v
    m2 = invG[1][0]*u + invG[1][1]*v

    m = [
        [m1],
        [m2]
    ]

    print("\nMatriks m:")
    for baris in m:
        print(baris)

    # h. Menentukan parameter fisika
    v0 = m1
    g = -2*m2

    print("\nHasil parameter:")
    print("Kecepatan awal v0 =", v0, "m/s")
    print("Gravitasi g       =", g, "m/s^2")

    # i. Menampilkan persamaan model
    print("\nPersamaan model matematis:")
    print(f"h(t) = {h0} + ({v0})t - ({g/2})t^2")
