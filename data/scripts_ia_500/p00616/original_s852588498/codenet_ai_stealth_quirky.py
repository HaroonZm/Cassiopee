def HOLE(Query,N):
    Dir = Query[0]
    A,B = (int(i)-1 for i in Query[1:])
    result=[]
    if Dir=='xy':
        result=[B*N+A+Z*N**2 for Z in xrange(N)]
    elif Dir=='xz':
        result=[N**2*B+A+Y*N for Y in xrange(N)]
    else:
        result=[N**2*B+A*N+X for X in xrange(N)]
    return result

while True:
    N,H = map(int, raw_input().split())
    if N == 0:
        break
    Bad = []
    for _ in range(H):
        Q = raw_input().split()
        Bad += HOLE(Q,N)
    Hset = set(Bad)
    print N**3 - len(Hset)