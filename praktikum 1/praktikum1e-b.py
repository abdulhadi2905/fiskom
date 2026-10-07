x = float(input("Nilai sudut : "))
x = x * (22 / 7) / 180
sinx = float(input("Nilai sin (x) : "))
print(f"{'Iterasi ke':<15}{'Hasil Perhitungan':<25}{'Selisih Harga Iterasi'}")
for m in range(1, 36):
    s = 0.0  # Reset jumlah deret untuk iterasi m baru
    j = 0    # Reset penghitung tanda untuk iterasi m baru 
    for i in range(0, 2 * m):
        if i % 2 == 1:
            j = j + 1
            if j % 2 == 0:
                td = -1
            else:
                td = 1   
            fn = 1.0
            fk = 1.0
            for k in range(1, i + 1):
                fn = fn * x
                fk = fk * k    
            s = s + td * (fn / fk) 
    d = abs(sinx - s)
    print(f"{m:<15}{s:<25}{d}")