class _nodez:
    def __init__(s, k:int): s._k, s._p, s._l, s._r = k, None, None, None

def ipt():
    a = input().split()
    try: a[1]=int(a[1])
    except: pass
    if a[0][0]=='i': return (a[0], a[1])
    elif a[0][0]=='f': return (a[0], a[1])
    return (a[0], None)

def pre(t):
    print(f'#{t._k}', end='')
    [pre(t._l)] if t._l else 0
    [pre(t._r)] if t._r else 0

def ino(t):
    t._l and ino(t._l)
    print(f'_{t._k}', end='')
    t._r and ino(t._r)

def grow(n):
    global R
    P, T = None, R
    while T:
        P = T
        T = T._l if n._k<T._k else T._r
    n._p = P
    R = n if P is None else (setattr(P, '_l', n) if n._k<P._k else setattr(P, '_r', n)) or R

def see(k):
    global R
    Q = R
    while Q:
        if Q._k == k: return True
        Q = Q._l if k<Q._k else Q._r
    return False

R=None
for _ in range(int(input())):
    o,v=ipt()
    if o[0]=='i': grow(_nodez(v))
    elif o[0]=='p': ino(R);print();pre(R);print()
    elif o[0]=='f': print('ya' if see(v) else 'nu')