x = float(input(" X : "))
p = float(input(" P : "))
Fp = float(input("Fp : "))
for m in range(1,36):
    s = 0.0
    j = 0.0
    for i in range(0,m):
        j = j + 1
        if j % 2 == 0:
            td = -1
        else:
            td =1
        fp = 1.0
        fn = 1.0
        fk = 1.0
        for k in range(1, i+1):
            fp = fp * (p - (k - 1))
            fn = fn * x
            fk = fk * k
        s = s + td*(fp*fn)/fk
    d = abs(Fp - s)
    print(f"{m:<15}{s:<25}{d}")