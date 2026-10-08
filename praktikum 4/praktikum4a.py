# INTERPOLASI BEDA SAMA NEWTON

# Input jumlah data
N = int(input("Jumlah data (N) : "))

# Input data X dan f(X)
X = []
F = []

for i in range(N):
    x = float(input(f"X[{i+1}] : "))
    fx = float(input(f"f(X[{i+1}]) : "))

    X.append(x)
    F.append([fx])

# Membuat tabel beda hingga
j = 0

while j < N - 1:
    j = j + 1
    i = 0

    while i < N - j:
        beda = F[i + 1][j - 1] - F[i][j - 1]
        F[i].append(beda)
        i = i + 1

# Menampilkan tabel beda hingga
print("\nTabel Beda Hingga")
print("----------------------------------------")

for i in range(N):
    print(f"{X[i]:10.4f}", end="")

    for j in range(len(F[i])):
        print(f"{F[i][j]:15.6f}", end="")

    print()

# Input nilai x yang ingin dicari
Xc = float(input("\nMasukkan nilai x yang ingin dicari : "))

# Jarak antar titik
h = X[1] - X[0]

# Nilai u
u = (Xc - X[0]) / h

# Perhitungan interpolasi Newton Beda Sama
y = F[0][0]
suku = 1.0
faktor = 1.0

for j in range(1, N):

    suku = suku * (u - (j - 1))
    faktor = faktor * j

    y = y + (suku / faktor) * F[0][j]

# Menampilkan hasil
print("\nHasil Interpolasi Beda Sama Newton")
print("----------------------------------------")
print("x =", Xc)
print("f(x) =", y)