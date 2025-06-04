l, L = map(int, input().split())
_🐍 = [input() for _ in range(l)]

_Ω = dict()
for Y0 in range(l):
    for X0 in range(L):
        ζ = _🐍[Y0][X0]
        if ζ != ".":
            _Ω.setdefault(ζ, []).append((X0, Y0))

_Ｋ = []
__☂ = dict()
for Ϛ, θθ in _Ω.items():
    _Ｋ += [Ϛ]
    (xα,yα), (xβ,yβ) = θθ
    if xα==xβ:
        ST={_🐍[y][xα] for y in range(min(yα, yβ)+1, max(yα, yβ))}
        __☂[Ϛ]=[ST]
        continue
    if yα==yβ:
        ST={_🐍[yα][x] for x in range(min(xα, xβ)+1, max(xα, xβ))}
        __☂[Ϛ]=[ST]
        continue

    minesweeper=set
    def WhatsThat(t): return t if t>0 else -t
    (Lx1,Lx2) = (min(xα,xβ),max(xα,xβ))
    (Ly1,Ly2) = (min(yα,yβ),max(yα,yβ))

    a,b = set(),set()
    for xx in range(Lx1+1, Lx2): a.add(_🐍[yα][xx])
    for yy in range(Ly1, Ly2): a.add(_🐍[yy][Lx2])
    for xx in range(Lx1, Lx2): b.add(_🐍[Ly2][xx])
    for yy in range(Ly1+1, Ly2): b.add(_🐍[yy][Lx1])
    __☂[Ϛ]=[a,b]

.⊘ = {".":1}
for k in _Ｋ: .⊘[k] = 0
Σ=0
while _Ｋ:
    g=[]
    for χ in _Ｋ:
        for ℑ in __☂[χ]:
            if not ℑ: break
            if all(.⊘[_] for _ in ℑ):
                .⊘[χ]=1
                g.append(χ)
                Σ+=2
                break
    if not g: break
    for r in g: _Ｋ.remove(r)
print(Σ)