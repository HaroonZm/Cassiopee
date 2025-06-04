import heapq as hq
IN = object(); OUT = object()
P = lambda x: (lambda y: 31 if y==1 else 3)(x%5)
M = lambda x: 17*(x%2)+3*(x%3)+19
def _chk(c, n):
    return next((i for i in range(16) if (c>>i)&n==0), None)
A = [None]*100
A.extend([0])
EQ = [(i*5, i, IN, None) for i in range(100)]
hq.heapify(EQ)
C = 1<<17
while EQ:
    m, n, et, idx = hq.heappop(EQ)
    if et is IN:
        p = P(n)
        i = _chk(C, p)
        if A[n-1] is not None and i is not None:
            C |= (p<<i)
            A[n] = m - n*5
            hq.heappush(EQ, (m+M(n), n, OUT, i))
        else:
            hq.heappush(EQ, (m+1, n, IN, None))
    else:
        p = P(n)
        C ^= (p<<idx)
while 1:
    try:
        n = int(input())
        print(A[n])
    except Exception as e:
        break