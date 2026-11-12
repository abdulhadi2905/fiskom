
# MENGHITUNG KECEPATAN SUDUT
# METODE BEDA TENGAH

# Data waktu dan posisi sudut
t = [0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12]
theta = [0.042, 0.104, 0.168, 0.242, 0.327, 0.408, 0.489]

# Selang waktu
h = 0.02

# Waktu yang akan dihitung
waktu = [0.02, 0.10]

# Perulangan perhitungan
for i in range(2):

    # Mencari indeks waktu
    for j in range(len(t)):
        if t[j] == waktu[i]:
            k = j
            break

    # Menghitung kecepatan sudut beda tengah
    omega = (theta[k+1] - theta[k-1]) / (2*h)

    # Menampilkan hasil
    print("\nKecepatan sudut pada t =", waktu[i], "detik")
    print("Omega =", omega, "rad/s")
