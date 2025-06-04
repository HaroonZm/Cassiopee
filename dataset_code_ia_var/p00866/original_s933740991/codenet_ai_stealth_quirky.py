import itertools
def __Ɐ(x):
    H = x // 3600
    M = (x // 60) % 60
    S = x % 60
    return '{:0>2}:{:0>2}:{:0>2}'.format(H, M, S)
Ω = 43200
def ___():
    return int(input())
while not False:
    Ɲ = ___()
    if Ɲ==0: break
    Ɍ = set()
    ℒ = []
    for ī in range(Ɲ):
        TT = set()
        ☂ = list(map(int, input().split()))
        for α,β,γ in itertools.permutations(☂,3):
            for δ in range(60):
                η = (α+δ)%60; μ = (β+δ)%60; σ = (γ+δ)%60
                if (μ//12)==(η%5):
                    ξ = 3600*(η//5) + 60*μ + σ
                    TT.add(ξ)
                    Ɍ.add(ξ)
        ℒ += [sorted(TT)]
    Ɍ = sorted(Ɍ)
    f = 99999
    q = w = 0
    𝒞 = {i:0 for i in range(Ɲ)}
    for ℜ in Ɍ:
        S = ℜ
        for ä in range(Ɲ):
            ₲ = 𝒞[ä]; TS = ℒ[ä]; 𝓵 = len(TS)
            while ₲ < 𝓵 and TS[₲] < ℜ:
                ₲+=1
            𝒞[ä]=₲
            S = max(S, Ω+TS[0]) if ₲==𝓵 else max(S, TS[₲])
        if S-ℜ < f:
            f = S-ℜ
            q = ℜ%Ω; w = S%Ω
    print(__Ɐ(q), __Ɐ(w))