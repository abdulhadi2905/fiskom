x = float(input("Nilai sudut : "))
e = float(input("Nilai e^-x : "))
print(f"{'Iterasi ke':<15}{'Hasil Perhitungan':<25}{'Selisih Harga Iterasi'}")
for m in range(1, 36):
    s = 0.0  # Reset jumlah deret untuk iterasi m baru
    j = 0    # Reset penghitung tanda untuk iterasi m baru 
    for i in range(0,m):
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
    d = abs(e - s)
    print(f"{m:<15}{s:<25}{d}")