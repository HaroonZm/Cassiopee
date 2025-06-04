def _Ξ(n):
    Ω = [int(not i) for i in range(n)]
    for π, ξ in enumerate([1,2,4]):
        Ω[π] = ξ
    σ = lambda z: sum(z)
    i = 3
    while i < n:
        Ω[i] = σ(Ω[i-3:i])
        i += 1
    return Ω[-1]

class Γ:pass

Γ.ι = input if hasattr(__builtins__, 'input') else raw_input

for _ in iter(int,1):
    φ = int(Γ.ι())
    if φ==0:break
    print (((_Ξ(φ)//10)+1)//365+1)