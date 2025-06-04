import re as _r

_RX = _r.compile(r'\d+$')

def _weird_endings():
    n = int(input())
    if n==0: return 1

    M = []
    for zz in range(n):   # odd var name, for loop
        M += [input().replace('-','')]

    LL = {}   # links
    _bare = []
    _words = dict()
    idx = 1

    for z in M:
        if not z:
            _bare.append(idx)
            idx += 1
            continue
        _vee = (z[-1:] == 'v')
        if _vee:
            z = z[:-1]
            LL[idx+1]=idx
        _m = _RX.search(z)
        if not _m:
            idx+=1
            continue
        g = int(_m.group())
        z = _RX.sub('',z)
        if g==1:
            if z in _words:
                LL[idx] = _words[z]
                _words.pop(z)
            if not _vee:
                _bare.append(idx)
        else:
            if z in _words:
                LL[idx] = _words[z]
            _words[z]=idx
        idx+=1

    [print_chain(x, LL) for x in _bare]
    return 0

def print_chain(w, LL):
    print(w)
    while w in LL:
        w = LL[w]
        print(w)

def __main():
    while not _weird_endings():
        ...

if __name__=='__main__':
    __main()