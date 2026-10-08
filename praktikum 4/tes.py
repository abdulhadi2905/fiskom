# INTERPOLASI SPLINE KUBIK ALAMI

# Input jumlah data
N = int(input("Jumlah data (N) : "))

# Input data X dan Y
X = []
Y = []

for i in range(N):
    x = float(input(f"X[{i+1}] : "))
    y = float(input(f"Y[{i+1}] : "))
    X.append(x)
    Y.append(y)

# Input nilai x yang akan dicari
Xc = float(input("\nMasukkan nilai x yang ingin dicari : "))

# 1. Menghitung jarak antar titik (h)
h = [X[i + 1] - X[i] for i in range(N - 1)]

# 2. Menyusun Sistem Persamaan Tridiagonal untuk mencari koefisien c
# A * c = B
alpha = [0.0] * N
for i in range(1, N - 1):
    alpha[i] = (3 / h[i]) * (Y[i + 1] - Y[i]) - (3 / h[i - 1]) * (Y[i] - Y[i - 1])

l = [1.0] * N
mu = [0.0] * N
z = [0.0] * N

# Penyelesaian algoritma Thomas untuk matriks tridiagonal
for i in range(1, N - 1):
    l[i] = 2 * (X[i + 1] - X[i - 1]) - h[i - 1] * mu[i - 1]
    mu[i] = h[i] / l[i]
    z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

# Inisialisasi koefisien
a = [Y[i] for i in range(N - 1)]
b = [0.0] * (N - 1)
c = [0.0] * N
d = [0.0] * (N - 1)

# Kondisi Natural Spline: c[N-1] = 0 dan c[0] = 0
c[N - 1] = 0.0

# Substitusi mundur untuk mendapatkan koefisien c, b, dan d
for j in range(N - 2, -1, -1):
    c[j] = z[j] - mu[j] * c[j + 1]
    b[j] = (Y[j + 1] - Y[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
    d[j] = (c[j + 1] - c[j]) / (3 * h[j])

# 3. Mencari interval tempat Xc berada dan menghitung nilainya
for i in range(N - 1):
    if X[i] <= Xc <= X[i + 1]:
        dx = Xc - X[i]

        # Persamaan spline kubik: S_i(x) = a_i + b_i*(dx) + c_i*(dx)^2 + d_i*(dx)^3
        Yc = a[i] + b[i] * dx + c[i] * (dx ** 2) + d[i] * (dx ** 3)

        # Menampilkan persamaan
        print("\nPersamaan Spline Kubik")
        print("----------------------")
        print(
            f"S_{i+1}(x) = {a[i]:.4f} + {b[i]:.4f}*(x - {X[i]}) "
            f"+ {c[i]:.4f}*(x - {X[i]})^2 + {d[i]:.4f}*(x - {X[i]})^3"
        )

        # Menampilkan hasil
        print("\nHasil Interpolasi")
        print("-----------------")
        print(f"x    = {Xc}")
        print(f"f(x) = {Yc:.4f}")

        break