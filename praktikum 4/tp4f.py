# INTERPOLASI SPLINE LINEAR

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

# Mencari interval Xc
for i in range(N - 1):

    if X[i] <= Xc <= X[i + 1]:

        # Persamaan spline linear
        Yc = Y[i] + (
            (Y[i + 1] - Y[i])
            / (X[i + 1] - X[i])
        ) * (Xc - X[i])

        # Menampilkan persamaan
        print("\nPersamaan Spline Linear")
        print("-----------------------")

        print(
            f"S{i+1}(x) = {Y[i]} + "
            f"(({Y[i+1]} - {Y[i]}) / "
            f"({X[i+1]} - {X[i]}))"
            f"(x - {X[i]})"
        )

        # Menampilkan hasil
        print("\nHasil Interpolasi")
        print("-----------------")
        print("x  =", Xc)
        print("f(x) =", Yc)

        break