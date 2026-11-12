
# MENGHITUNG LAJU ALIRAN KALOR PADA BATANG

# Input data
K = float(input("Masukkan konduktivitas termal (K): "))
A = float(input("Masukkan luas penampang (A): "))

x = [2, 20]

for i in range(2):

    X = x[i]

    # Reduksi sudut
    sudut = X

    while sudut > 3.141592653589793:
        sudut = sudut - 6.283185307179586

    # Menghitung e^(-1) dengan deret Taylor
    exp1 = 1
    suku = 1

    for n in range(1, 31):
        suku = suku * (-1) / n
        exp1 = exp1 + suku

    # Menghitung e^(-x^2) dengan pemangkatan
    exp = exp1 ** (X**2)

    # Menghitung cos(x)
    cosx = 1
    suku = 1

    for n in range(1, 21):
        suku = suku * (-sudut**2) / ((2*n-1)*(2*n))
        cosx = cosx + suku

    # Menghitung turunan temperatur
    dT = exp * (1 - 2*X**2) - 1 / cosx**2

    # Menghitung laju aliran kalor
    Q = -K * A * dT

    # Menampilkan hasil
    print("\nHasil Perhitungan pada x =", x[i], "mm")
    print("Turunan temperatur =", dT)
    print("Laju aliran kalor  =", Q)
