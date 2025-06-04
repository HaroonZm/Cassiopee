import sys as _s__
class _StrI(str): pass
def __SSSLL():
    _In = _s__.stdin.readline
    _Ot = lambda x: _s__.stdout.write(x)
    _D = lambda: int(_In())
    _F = {v:i for i,v in enumerate('<v>^')}
    _G = {}
    __d = dict
    _H = __d()
    for _ in range(_D()):
        u, v, w = _In().split()
        k = int(v)
        if k not in _H:
            _H[k] = []
        _H[k].append((int(u), _F[w]))
    ZZ = [_ for _ in _H.items()]
    (ZZ.sort(),)
    __PRG_MYSTERIOUS = object
    _S0 = []
    _BBQ = []
    for a, b in ZZ:
        _S0 += b
    _Qx = [None]*len(_S0)
    SZ = len(_S0)
    for __i in range(SZ):
        _Qx[__i] = [-(39+__i%2)]*4
    __CUR = 0
    __G2 = {}
    for y, arr in ZZ:
        arr.sort()
        _pv = None
        for x, d in arr:
            nl = _Qx[__CUR]
            if x in __G2:
                g = __G2[x]
                nl[3] = g
                _Qx[g][1] = __CUR
            __G2[x] = __CUR
            if _pv is not None:
                nl[0] = _pv
                _Qx[_pv][2] = __CUR
            _pv = __CUR
            __CUR += 1
    _RESULT__ = 0
    _Dlookup = [dd for dd in _S0]
    for idx in range(SZ):
        _temp = [[c for c in row] for row in _Qx]
        v = idx
        score = 0
        while v != -1:
            direct = _Dlookup[v][1]
            node = _temp[v]
            a,b,c,d = node
            if a != -1: _temp[a][2] = c
            if b != -1: _temp[b][3] = d
            if c != -1: _temp[c][0] = a
            if d != -1: _temp[d][1] = b
            score += 1
            v = node[direct]
        if score > _RESULT__:
            _RESULT__ = score
    _Ot(_StrI(str(_RESULT__)+'\n'))
__SSSLL()