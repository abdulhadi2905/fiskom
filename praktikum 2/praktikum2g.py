# Fungsi Determinan bawaan untuk menghitung D dan DY
def hitung_determinan(matriks, n):
  if n == 1:
    return matriks[0][0]
  if n == 2:
    return matriks[0][0] * matriks[1][1] - matriks[0][1] * matriks[1][0]

  det = 0
  for c in range(n):
    sub = []
    for i in range(1, n):
      baris = []
      for j in range(n):
        if j != c:
          baris.append(matriks[i][j])
      sub.append(baris)
    tanda = 1 if c % 2 == 0 else -1
    det += tanda * matriks[0][c] * hitung_determinan(sub, n - 1)
  return det


# 1. INVERS B, X, Z (Input Ordo & Matriks X)
b = int(input("Masukkan ordo matriks (b): "))

print("\nMasukkan elemen matriks X:")
x = []
for i in range(b):
  baris = []
  for j in range(b):
    baris.append(float(input(f"X({i+1},{j+1}): ")))
  x.append(baris)

# 2. Hitung Determinan Utama D
D = hitung_determinan(x, b)

# Inisialisasi Matriks Hasil Invers Z
Z = [[0.0 for _ in range(b)] for _ in range(b)]

# 3. Process Loop i = 1..b
for i in range(b):
  # Loop j = 1..b
  for j in range(b):
    m = 0
    n = 0
    # Matriks kofaktor/minor y berukuran (b-1) x (b-1)
    y = [[0.0 for _ in range(b - 1)] for _ in range(b - 1)]

    # Loop k = 1..b
    for k in range(b):
      # Kondisi i <> k (i != k)
      if i != k:
        n = 0
        # Loop l = 1..b
        for l in range(b):
          # Kondisi j <> l (j != l)
          if j != l:
            y[m][n] = x[k][l]
            n = n + 1
        m = m + 1

    # Connector 3, 4, 5

    # Hitung Determinan Kofaktor DY
    DY = hitung_determinan(y, b - 1)

    # Kondisi (i+j)/2 sisa bagi 0 (Pengecekan Kebentukan Genap/Ganjil Indeks)
    # Penyesuaian indeks Python (0-based) ke flowchart (1-based): (i+1)+(j+1)
    if ((i + 1) + (j + 1)) % 2 == 0:
      t = 1
    else:
      t = -1

    # Z(J,I) = T * DY / D (Invers menggunakan Adjoint Transpose Z_ji)
    Z[j][i] = t * DY / D

# 4. Connector 2 -> Tulis Z(J,I) & END
print("\nHasil Invers Matriks Z:")
for i in range(b):
  for j in range(b):
    print(f"Z({i+1},{j+1}) = {Z[i][j]:.4f}", end="\t")
  print()