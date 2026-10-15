
# PERBANDINGAN PERSAMAAN VAN DER WAALS
# DAN PERSAMAAN GAS IDEAL

# Konstanta gas
R = 0.082054
T = 300
n = 1

# Konstanta Van der Waals
a = 1.360
b = 0.03183

# Tekanan yang akan dihitung
tekanan = [1, 10, 100]

# Fungsi menghitung volume dengan Van der Waals
def van_der_waals(p):

    # Nilai awal volume molar
    v = R * T / p

    # Iterasi Newton-Raphson
    for i in range(100):

        # Fungsi Van der Waals
        f = (p + a / v**2) * (v - b) - R * T

        # Turunan fungsi terhadap v
        df = p - a / v**2 + 2 * a * b / v**3

        # Menghindari pembagian dengan nol
        if abs(df) < 1e-12:
            break

        # Menghitung volume berikutnya
        v_baru = v - f / df

        # Memeriksa konvergensi
        if abs(v_baru - v) < 1e-10:
            v = v_baru
            break

        v = v_baru

    return v * n


# Menampilkan tabel Van der Waals
print("Persamaan Van der Waals")
print("-" * 45)
print(f"{'Tekanan (atm)':<20}{'Volume tabung (liter)':>25}")

for p in tekanan:
    V = van_der_waals(p)
    print(f"{p:<20}{V:>25.6f}")


# Menampilkan tabel Gas Ideal
print("\nPersamaan Gas Ideal")
print("-" * 45)
print(f"{'Tekanan (atm)':<20}{'Volume tabung (liter)':>25}")

for p in tekanan:
    V = n * R * T / p
    print(f"{p:<20}{V:>25.6f}")
