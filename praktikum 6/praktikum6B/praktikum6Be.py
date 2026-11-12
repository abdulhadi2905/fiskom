
# SIMULASI PELURUHAN ZAT RADIOAKTIF
# METODE NUMERIK EULER

# Input data
N0 = float(input("Masukkan jumlah zat awal (N0): "))
lamda = float(input("Masukkan konstanta peluruhan (lambda): "))
dt = float(input("Masukkan selang waktu (delta t): "))
tmax = float(input("Masukkan waktu akhir simulasi: "))

# Inisialisasi
N = N0
t = 0
n = 0

# Menampilkan hasil
print("\nHASIL SIMULASI PELURUHAN RADIOAKTIF")
print("---------------------------------------------")
print(f"{'Iterasi':<12}{'Waktu':<15}{'Jumlah zat':<20}")

while t <= tmax:

    # Menampilkan jumlah zat saat ini
    print(f"{n:<12}{t:<15.4f}{N:<20.8f}")

    # Menghitung jumlah zat berikutnya
    N = N - lamda * N * dt

    # Menambah waktu dan iterasi
    t = t + dt
    n = n + 1

print("---------------------------------------------")
print("Simulasi selesai")
