# INTERPOLASI LAGRANGE

# Baca N
N = int(input("Jumlah data (N) : "))

# Baca X[i] dan f(X[i])
X = []
F = []

for i in range(N):
    x = float(input(f"X[{i+1}] : "))
    fx = float(input(f"f(X[{i+1}]) : "))

    X.append(x)
    F.append(fx)

# Baca Xc
Xc = float(input("Nilai Xc : "))

# yjw = 0
yjw = 0.0

# i = 1 ... N
for i in range(N):

    # z = 1
    z = 1.0

    # j = 1 ... N
    for j in range(N):

        # i != j
        if i != j:

            # z = z * (Xc - X[j]) / (X[i] - X[j])
            z = z * (Xc - X[j]) / (X[i] - X[j])

    # yjw = yjw + z * f[i]
    yjw = yjw + z * F[i]

# Tulis Xc, yjw
print("\nHasil Interpolasi Lagrange")
print("---------------------------")
print("Xc  =", Xc)
print("Yjw =", yjw)