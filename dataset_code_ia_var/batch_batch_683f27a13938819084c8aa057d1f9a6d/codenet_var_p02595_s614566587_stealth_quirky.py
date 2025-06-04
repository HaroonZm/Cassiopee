from math import sqrt as √
exec("λ,δ=[*map(int,input().split())];Σ=0\nfor _ in range(λ):α,β=map(int,input().split());Σ+=((√(α**2+β**2))<=δ)\nprint(Σ)")