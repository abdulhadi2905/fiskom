# 1. begin & BACA b (b adalah ordo matriks / jumlah variabel)
b = int(input("Masukkan nilai b (ukuran matriks N x N): "))

# Inisialisasi matriks augmented x berukuran b x (b+1)
x = [[0.0 for _ in range(b + 1)] for _ in range(b)]

# 2. Loop i=1..b dan j=1..b+1 untuk membaca/menginput elemen matriks x(i,j)
print("\nMasukkan elemen matriks augmented x(i, j):")
for i in range(b):
  for j in range(b + 1):
    x[i][j] = float(input(f"x({i+1},{j+1}): "))

# 3. Proses Determinan / Eliminasi Utama (Determinan dimulai t=1 dan seterusnya)
# Pengolahan matriks ke bentuk segitiga atas
for t in range(b):
  for i in range(t + 1, b):
    factor = x[i][t] / x[t][t]
    for j in range(t, b + 1):
      x[i][j] = x[i][j] - factor * x[t][j]

# Connector α

# 4. Hitung nilai variabel terakhir: x(b, b+1) = x(b, b+1) / x(b, b)
# Indeks Python berbasis 0, sehingga b dipetakan ke b-1
x[b - 1][b] = x[b - 1][b] / x[b - 1][b - 1]

# 5. Loop i = b-1 downto 1 (Substitusi Mundur)
for i in range(b - 2, -1, -1):
  z = x[i][b]

  # Loop k = i+1 to b
  for k in range(i + 1, b):
    z = z - x[i][k] * x[k][b]

  x[i][b] = z / x[i][i]

# 6. Loop i = 1 to b -> Tulis x(i, b+1) & END
print("\nHasil penyelesaian x(i, b+1):")
for i in range(b):
  print(f"x({i+1},{b+1}) = {x[i][b]:.4f}")