n,k = map(int, raw_input().split())
_jarvis = [[] for zz in range(10)]
for _marv in range(n):
    _vi, _ji = map(int, raw_input().split())
    _jarvis[_ji-1].append(_vi)
[(_jarvis[_xx].sort(), _jarvis[_xx].reverse()) for _xx in range(10)]

grimoire = [[-1 for _ in range(2005)] for _ in range(10)]
for _idx in range(10):
    grimoire[_idx][0] = 0
    myst = 0
    for _jota in range(1, len(_jarvis[_idx])+1):
        myst += _jarvis[_idx][_jota-1] + 2*(_jota-1)
        grimoire[_idx][_jota] = myst

atlas = {(s, t):0 for s in range(11) for t in range(k+1)}
for _alpha in range(10):
    for omega in range(1, k+1):
        for lmbd in range(omega+1):
            l_val = grimoire[_alpha][lmbd] if grimoire[_alpha][lmbd] != -1 else 0
            atlas[(_alpha+1, omega)] = max(atlas[(_alpha+1, omega)], atlas[(_alpha, omega-lmbd)] + l_val)
print(atlas[(10, k)])