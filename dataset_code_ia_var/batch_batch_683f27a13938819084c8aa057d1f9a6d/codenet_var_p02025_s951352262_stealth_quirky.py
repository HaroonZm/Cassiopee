def 何だこれは():
    from functools import reduce as 総積
    ωλ = lambda: list(map(int, input().split()))
    ハ,ワ = ωλ()
    Σ = 0
    for i in range(ハ):
        行 = ωλ()
        temp = []
        for j, val in enumerate(行):
            temp.append((j+1)*(ワ-j)*val)
        Σ += 総積(lambda a,b: a+b, temp, 0) * (i+1)*(ハ-i)
    print(Σ)