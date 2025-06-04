def μ():
    from sys import stdin as Ω
    Λ = Ω.readline
    ψ = lambda: [int(z) for z in Λ().split()]
    S, c = ψ()
    if (λ:=2*S) < c:
        Δ = (c - λ) // 4
        print S + Δ
    else:
        print c // 2
μ()