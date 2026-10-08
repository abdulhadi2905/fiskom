# ==============================================================================
# PERBEDAAN UTAMA GAUSS VS GAUSS-JORDAN:
# 1. Eliminasi Maju:
#    - Gauss: Mengubah elemen di bawah diagonal utama menjadi 0 (bentuk segitiga atas).
#    - Gauss-Jordan: Mengubah elemen di bawah DAN di atas diagonal utama menjadi 0,
#      serta membagi baris pivot agar elemen diagonal utama menjadi 1.
# 2. Substitusi Belakang:
#    - Gauss: Membutuhkan loop substitusi mundur (Backward Substitution) untuk mencari nilai x.
#    - Gauss-Jordan: TIDAK memerlukan substitusi belakang, karena matriks A langsung
#      berubah menjadi matriks identitas. Nilai variabel langsung didapat dari kolom b.
# ==============================================================================

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

# 4. Eliminasi Gauss-Jordan (Membuat Matriks Identitas)
for i in range(N):
  # PERBEDAAN 1: Normalisasi baris pivot agar elemen diagonal utama (G[i][i]) bernilai 1
  pivot = G[i][i]
  for k in range(i, N + 1):
    G[i][k] = G[i][k] / pivot

  # PERBEDAAN 2: Meng-nol-kan seluruh baris pada kolom i KECUALI baris pivot (j != i)
  # (Pada Gauss biasa, loop j hanya dari i + 1 ke N)
  for j in range(N):
    if i != j:
      pem = G[j][i]
      for k in range(i, N + 1):
        G[j][k] = G[j][k] - pem * G[i][k]

# PERBEDAAN 3: Tidak ada Substitusi Belakang (Backward Substitution)!
# Nilai x langsung diambil dari kolom terakhir matriks G yang sudah tereduksi.
x = [0.0 for _ in range(N)]
for i in range(N):
  x[i] = G[i][N]

# 5. Tulis hasil & Selesai
print("\nHasil penyelesaian {x}:")
for i in range(N):
  print(f"x_{i+1} = {x[i]:.4f}")