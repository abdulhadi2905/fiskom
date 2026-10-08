# INTERPOLASI BEDA TIDAK SAMA NEWTON

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

# Membuat tabel beda terbagi
j = 0

while j < N - 1:
    j = j + 1
    i = 0

    while i < N - j:

        Fdiv = (F[i + 1][j - 1] - F[i][j - 1]) / (X[i + j] - X[i])

        F[i].append(Fdiv)

        i = i + 1

# Menampilkan tabel beda terbagi
print("\nTabel Beda Terbagi Newton")
print("----------------------------------------")

for i in range(N):
    print(f"{X[i]:10.4f}", end="")

    for j in range(len(F[i])):
        print(f"{F[i][j]:15.6f}", end="")

    print()

# Input nilai x yang ingin dicari
Xc = float(input("\nMasukkan nilai x yang ingin dicari : "))

# Perhitungan interpolasi Newton
y = F[0][0]
FA = 1.0

j = 0

while j < N - 1:

    j = j + 1

    # FA = FA * (Xc - X[j-1])
    FA = FA * (Xc - X[j - 1])

    # y = y + FA * beda terbagi
    y = y + FA * F[0][j]

# Menampilkan hasil
print("\nHasil Interpolasi Beda Tidak Sama Newton")
print("----------------------------------------")
print("x =", Xc)
print("f(x) =", y)