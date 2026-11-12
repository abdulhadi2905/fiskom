import matplotlib.pyplot as plt

# MENGHITUNG LAJU ALIRAN KALOR PADA BATANG

# Input data
K = float(input("Masukkan konduktivitas termal (K): "))
A = float(input("Masukkan luas penampang (A): "))

x = [2, 20]
daftar_dT = []  # Menyimpan nilai dT untuk keperluan visualisasi

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
    daftar_dT.append(dT)

    # Menghitung laju aliran kalor
    Q = -K * A * dT

    # Menampilkan hasil
    print("\nHasil Perhitungan pada x =", x[i], "mm")
    print("Turunan temperatur =", dT)
    print("Laju aliran kalor  =", Q)

# ==========================================================
# VISUALISASI PENGARUH K DAN A TERHADAP Q
# ==========================================================

# Membuat rentang variasi nilai K dan A (misal dari 0.2x hingga 2x nilai input)
variasi_K = [K * faktor for faktor in [0.2, 0.5, 0.8, 1.0, 1.3, 1.6, 2.0]]
variasi_A = [A * faktor for faktor in [0.2, 0.5, 0.8, 1.0, 1.3, 1.6, 2.0]]

# Menghitung Q untuk setiap variasi K (dengan A tetap)
Q_var_K_x2 = [-k_val * A * daftar_dT[0] for k_val in variasi_K]
Q_var_K_x20 = [-k_val * A * daftar_dT[1] for k_val in variasi_K]

# Menghitung Q untuk setiap variasi A (dengan K tetap)
Q_var_A_x2 = [-K * a_val * daftar_dT[0] for a_val in variasi_A]
Q_var_A_x20 = [-K * a_val * daftar_dT[1] for a_val in variasi_A]

# Membuat 2 subplot berdampingan
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Grafik 1: Pengaruh K terhadap Q (A konstan)
ax1.plot(variasi_K, Q_var_K_x2, marker='o', label=f'x = {x[0]} mm')
ax1.plot(variasi_K, Q_var_K_x20, marker='s', linestyle='--', label=f'x = {x[1]} mm')
ax1.set_title(f'Pengaruh K terhadap Q (A = {A} tetap)')
ax1.set_xlabel('Konduktivitas Termal, K')
ax1.set_ylabel('Laju Aliran Kalor, Q')
ax1.grid(True)
ax1.legend()

# Grafik 2: Pengaruh A terhadap Q (K konstan)
ax2.plot(variasi_A, Q_var_A_x2, marker='o', color='green', label=f'x = {x[0]} mm')
ax2.plot(variasi_A, Q_var_A_x20, marker='s', linestyle='--', color='orange', label=f'x = {x[1]} mm')
ax2.set_title(f'Pengaruh A terhadap Q (K = {K} tetap)')
ax2.set_xlabel('Luas Penampang, A')
ax2.set_ylabel('Laju Aliran Kalor, Q')
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()