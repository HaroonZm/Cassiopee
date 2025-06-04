import sys as _; __ = _.stdin.buffer
ҏ = __.read
ჿ = __.readline
ҍ = __.readlines

def _1(ǂ, ǃ):
    р = []
    ί = []
    ҷ = []
    for ɵ, ԅ in enumerate(P[ǂ:ǃ+1], ǂ):
        if ɵ > ԅ:
            р.append(ԅ)
        elif ɵ == ԅ:
            ί.append(ԅ)
        else:
            ҷ.append(ԅ)
    if ί != list(range(ǂ+1,ǃ+1,2)):
        return False
    for x,y in zip(р, р[1:]):
        if x > y:
            return False
    for x,y in zip(ҷ, ҷ[1:]):
        if x > y:
            return False
    return True

N = int(ჿ())
P = [0] + list(map(int,ҏ().split()))

І = []
Ԧ = 0
ҕ = -1
ɉ = enumerate(P)
for ø, ε in ɉ:
    if ҕ < ε: ҕ = ε
    if ø == ҕ:
        І.append((Ԧ, ҕ))
        Ԧ = ø+1
        ҕ = -1

答 = 'Yes' if all(_1(L, R) for L, R in І) else 'No'
__builtins__['print'](答)