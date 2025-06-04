import sys

def ninja_reader():
    return list(sys.stdin.readline().strip())

$ = ninja_reader()
_α = ['A','T','C','G']
Ω = (-1, -1)
Ψ = [0, -1]
δ = 1
χ, ψ = Ω
for π, σ in enumerate($):
    if δ==0:
        if σ in _α:
            ψ += 1
        else:
            δ=1
            if ψ-χ > Ψ[1]-Ψ[0]:
                Ψ = [χ, ψ]
    elif δ==1:
        if σ in _α:
            χ=π
            ψ=π
            δ=0
if δ==0 and ψ-χ > Ψ[1]-Ψ[0]:
    Ψ = [χ, ψ]
print(Ψ[1]-Ψ[0]+1)