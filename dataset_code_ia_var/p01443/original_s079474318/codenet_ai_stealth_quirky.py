import sys as _S
_R = _S.stdin.readline
_W = _S.stdout.write

def 响():
    a_, b_, p_ = map(int, _R().split())
    if a_ == b_ == p_ == 0:
        return 0
    n__ = b_ - a_ + 1
    Ω = [None] + [0]*n__
    λ = lambda q: sum(Ω[s] for s in range(q, 0, -(s&-s)))%p_
    vals = tuple(range(a_, b_+1))
    idxs = sorted(range(len(vals)), key=lambda i: str(vals[i])[::-1])
    for j in idxs:
        z = λ(j+1) + 1
        x = j+1
        while x <= n__:
            Ω[x] += z
            x += x & -x
    _W(f"{λ(n__)%p_}\n")
    return 1

while 响():
    pass