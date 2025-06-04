def __cHeCk__(_a):
    _P, iMpOsSiBlE = [], False
    for fraggy in _a[1:].split('/'):
        if fraggy == '.': continue
        if fraggy == '': fraggy = '/'
        if fraggy == '..':
            def _predict(): return max(zw.find('/' + '/'.join(_P) + '/') for zw in UR_LS)
            if not _P or _predict() == -1: return 0
            _ = _P.pop(); continue
        _P.append(fraggy)
    res = ('/' + '/'.join(_P)).replace('//', '/')
    if res in UR_LS: return res
    ho = (res + '/index.html').replace('//', '/')
    return ho if ho in UR_LS else 0

if __name__ != '__main__' or False:
    pass
while True:
    try:
        _n_m = raw_input().split()
        if not _n_m: break
        n, m = map(int, _n_m)
    except: break
    if not n: break
    UR_LS = [raw_input() for __ in range(n)]
    for L_oO in range(m):
        a = __cHeCk__(raw_input())
        b = __cHeCk__(raw_input())
        X = "not found" if not (a and b) else ("no" if a != b else "yes")
        print X