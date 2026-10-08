# INTERPOLASI SPLINE KUADRATIK

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

# Hitung koefisien a, b, dan c untuk setiap interval
a = [0.0] * (N - 1)
b = [0.0] * (N - 1)
c = [0.0] * (N - 1)

# Asumsi dasar spline kuadratik: a[0] = 0
a[0] = 0.0
c[0] = Y[0]
b[0] = (Y[1] - Y[0]) / (X[1] - X[0])

# Menghitung koefisien untuk interval sisanya (i = 1 s.d. N-2)
for i in range(1, N - 1):
    h_prev = X[i] - X[i - 1]
    c[i] = Y[i]
    
    # Syarat kontinuitas turunan pertama di titik simpul
    b[i] = 2 * a[i - 1] * h_prev + b[i - 1]
    
    # Menghitung nilai a[i] dari persamaan S_i(X[i+1]) = Y[i+1]
    h_curr = X[i + 1] - X[i]
    a[i] = (Y[i + 1] - Y[i] - b[i] * h_curr) / (h_curr ** 2)

# Mencari interval tempat Xc berada
for i in range(N - 1):
    if X[i] <= Xc <= X[i + 1]:
        dx = Xc - X[i]
        
        # Persamaan spline kuadratik: S_i(x) = a_i*(x - x_i)^2 + b_i*(x - x_i) + c_i
        Yc = a[i] * (dx ** 2) + b[i] * dx + c[i]

        # Menampilkan persamaan
        print("\nPersamaan Spline Kuadratik")
        print("--------------------------")
        print(f"S_{i+1}(x) = {a[i]:.4f}*(x - {X[i]})^2 + {b[i]:.4f}*(x - {X[i]}) + {c[i]:.4f}")

        # Menampilkan hasil
        print("\nHasil Interpolasi")
        print("-----------------")
        print(f"x    = {Xc}")
        print(f"f(x) = {Yc:.4f}")

        break