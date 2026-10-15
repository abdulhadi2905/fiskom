
# MENENTUKAN JARI-JARI KELENGKUNGAN JALAN
# Metode Newton-Raphson

# Data yang diketahui
T = float(input("Masukkan jarak tangensial T (m): "))
M = float(input("Masukkan ordinat titik tengah M (m): "))
R = float(input("Masukkan nilai awal R (m): "))

imax = 15

print("\nHasil Iterasi Newton-Raphson")
print(f"{'N':<10}{'R(n) (m)':<20}{'Error (m)':<20}")

for n in range(1, imax + 1):

    # Fungsi dari persamaan awal
    fR = R - R**2 / (R**2 + T**2)**0.5 - M

    # Turunan pertama fungsi
    dfR = (
        1
        - 2*R / (R**2 + T**2)**0.5
        + R**3 / (R**2 + T**2)**1.5
    )

    # Pemeriksaan pembagian dengan nol
    if abs(dfR) < 1e-12:
        print("Turunan mendekati nol. Iterasi dihentikan.")
        break

    # Iterasi Newton-Raphson
    R_baru = R - fR / dfR

    # Menghitung error
    error = abs(R_baru - R)

    print(f"{n:<10}{R_baru:<20.10f}{error:<20.10f}")

    R = R_baru

    if error < 1e-8:
        break

# Memeriksa kembali persamaan awal
sisa = R - R**2 / (R**2 + T**2)**0.5 - M

print("\nJari-jari kelengkungan jalan =", R, "m")
print("Nilai fungsi pada hasil akhir =", sisa)
