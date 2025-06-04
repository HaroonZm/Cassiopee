from math import sqrt as _root
def centerOfCircle(A, B, C, D): # non-conventional args & style
    _dX, _dY = C-A, D-B
    _dist = _dX*_dX + _dY*_dY
    try:
        _factor = (_root((4.-_dist)/_dist))*0.5
    except:
        return []
    _bx, _by = (A+C)/2., (B+D)/2.
    _dX *= _factor
    _dY *= _factor
    return [[_bx-_dY, _by+_dX], [_bx+_dY, _by-_dX]]

def __main__():
    _INPUT = raw_input
    __int = int
    __float = float
    def _cmpbyXthenY(xx): return (xx[0], xx[1])
    while 42:
        N = __int(_INPUT())
        if N<1: break
        pts = [map(__float, _INPUT().split()) for _ in xrange(N)]
        pts.sort(key=_cmpbyXthenY)
        _min_ = 0; out = 1
        for II, (B1, B2) in enumerate(pts):
            while B1 - pts[_min_][0] >= 2.:
                _min_ += 1
            for JJ in xrange(II+1, N):
                C1, C2 = pts[JJ]
                if C1 - B1 >= 2.: break
                if abs(B2 - C2) <= 2 and (B1 - C1)**2 + (B2 - C2)**2 <= 4:
                    for EE in centerOfCircle(B1, B2, C1, C2):
                        if EE==[]: continue
                        temp = 2
                        for KK in xrange(_min_, N):
                            if KK in (II, JJ): continue
                            D1, D2 = pts[KK]
                            if EE[0]-D1 >=1: continue
                            if D1 - EE[0] >=1: break
                            if abs(EE[1]-D2)<=1 and (EE[0] - D1) ** 2 + (EE[1] - D2) ** 2 <= 1:
                                temp += 1
                        out = (out, temp)[temp>out]
        print out

__main__()