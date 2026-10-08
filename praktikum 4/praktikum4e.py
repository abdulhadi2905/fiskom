# INTERPOLASI SPLINE KUBIK (NATURAL CUBIC SPLINE)

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

n = N - 1
h = [X[i + 1] - X[i] for i in range(n)]

# Koefisien a_i = Y_i
a = Y[:n]

# Membangun Sistem Persamaan Linear Tridiagonal untuk mencari koefisien c
alpha = [0.0] * N
for i in range(1, n):
    alpha[i] = (3 / h[i]) * (Y[i + 1] - Y[i]) - (3 / h[i - 1]) * (Y[i] - Y[i - 1])

# Menggunakan Algoritma Thomas (Tridiagonal Matrix Algorithm / TDMA)
l = [1.0] + [0.0] * n
mu = [0.0] * N
z = [0.0] * N

for i in range(1, n):
    l[i] = 2 * (X[i + 1] - X[i - 1]) - h[i - 1] * mu[i - 1]
    mu[i] = h[i] / l[i]
    z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

l[n] = 1.0
z[n] = 0.0

c = [0.0] * N
b = [0.0] * n
d = [0.0] * n

# Inisialisasi batas Natural Spline (c[N-1] = 0)
c[n] = 0.0

# Substitusi balik untuk menghitung koefisien b, c, dan d
for j in range(n - 1, -1, -1):
    c[j] = z[j] - mu[j] * c[j + 1]
    b[j] = (Y[j + 1] - Y[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
    d[j] = (c[j + 1] - c[j]) / (3 * h[j])

# Mencari interval tempat Xc berada dan menghitung nilai Yc
for i in range(n):
    if X[i] <= Xc <= X[i + 1]:
        dx = Xc - X[i]
        
        # Persamaan Spline Kubik: S_i(x) = a_i + b_i*(x - x_i) + c_i*(x - x_i)^2 + d_i*(x - x_i)^3
        Yc = a[i] + b[i] * dx + c[i] * (dx ** 2) + d[i] * (dx ** 3)

        # Menampilkan persamaan
        print("\nPersamaan Spline Kubik")
        print("----------------------")
        print(f"S_{i+1}(x) = {a[i]:.4f} + {b[i]:.4f}*(x - {X[i]}) + {c[i]:.4f}*(x - {X[i]})^2 + {d[i]:.4f}*(x - {X[i]})^3")

        # Menampilkan hasil
        print("\nHasil Interpolasi")
        print("-----------------")
        print(f"x    = {Xc}")
        print(f"f(x) = {Yc:.4f}")

        break