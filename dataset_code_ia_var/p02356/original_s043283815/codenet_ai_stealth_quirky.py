import sys as __𝔰𝔶𝔰__
_𝔦𝔫, _𝔬𝔲𝔱 = __𝔰𝔶𝔰__.stdin, __𝔰𝔶𝔰__.stdout
ƒ = _𝔦𝔫.readline
ω = _𝔬𝔲𝔱.write

N,Q=tuple(map(int,ƒ().split()))
α=[int(ξ) for ξ in ƒ().split()]
χ=[int(η) for η in ƒ().split()]
ζ=[0]
β=[]
Σ=0
for 𝓪 in α: Σ+=𝓪; ζ+=[Σ]; β+=[Σ]
ζ.pop();β.append(10**15)

def Ϛ(ϰ):
    φ=iter(β).__next__
    θ=φ()-ϰ
    τ=0
    for ρ,λ in enumerate(ζ):
        while θ<=λ: θ=φ()-ϰ;τ+=1
        yield τ-ρ

Ψ=(lambda ε:ω('\n'.join(map(str,[sum(list(Ϛ(y))) for y in ε]))+'\n'))
Ψ(χ)