# 1. Mulai & Baca [A], {b} dari Input User
N = int(input("Masukkan jumlah persamaan / ukuran matriks (N): "))

print("\nMasukkan elemen matriks A (baris demi baris):")
A = []
for i in range(N):
  baris = []
  for j in range(N):
    nilai = float(input(f"A[{i+1}][{j+1}]: "))
    baris.append(nilai)
  A.append(baris)

print("\nMasukkan elemen vektor b:")
b = []
for i in range(N):
  nilai = float(input(f"b[{i+1}]: "))
  b.append(nilai)

# Inisialisasi matriks G berukuran N x (N+1)
G = [[0.0 for _ in range(N + 1)] for _ in range(N)]

# 2. Salin A ke G (i = 1..N, j = 1..N)
for i in range(N):
  for j in range(N):
    G[i][j] = A[i][j]

# 3. Salin b ke kolom terakhir G (G_j,n+1 = b_j)
for j in range(N):
  G[j][N] = b[j]

# 4. Eliminasi Maju
for i in range(N):
  for j in range(i + 1, N):
    pem = G[j][i] / G[i][i]
    for k in range(i, N + 1):
      G[j][k] = G[j][k] - pem * G[i][k]

# Connector A

# 5. Substitusi Belakang
x = [0.0 for _ in range(N)]

# x_n = G_n,n+1 / G_nn
x[N - 1] = G[N - 1][N] / G[N - 1][N - 1]

# Loop i = N-1 .. 1 (bergerak mundur)
for i in range(N - 2, -1, -1):
  Cad = G[i][N]
  # Loop j = i + 1 .. N
  for j in range(i + 1, N):
    Cad = Cad - G[i][j] * x[j]
  x[i] = Cad / G[i][i]

# 6. Tulis hasil & Selesai
print("\nHasil penyelesaian {x}:")
for i in range(N):
  print(f"x_{i+1} = {x[i]:.4f}")