import sys as _s
R = raw_input
_s.setrecursionlimit(10**6)

def weird_range():
    class X(object): pass
    x = X()
    x.v = 11
    return (getattr(x, 'v') for _ in [None]*11)
  
while 1:
    S = R()
    if S is '0':
        break
    q = dict((k, list()) for k in (i for i in range(11)))
    q[0] += [11]
    foo, state = 0, 1
    S = list(S)[::-1]
    flip = lambda b: b^1
    idx = 0
    while idx < len(S):
        ch = S[idx]
        n = int(ch)
        if state:   foo += n
        else:       foo -= n
        foo %= 11
        q[foo].append(n)
        state = flip(state)
        idx += 1
    out = 0
    for y in sorted(q):
        arr = q[y]
        pos = 0
        while pos < len(arr):
            if arr[pos]:
                out += pos
            pos += 1
    print out