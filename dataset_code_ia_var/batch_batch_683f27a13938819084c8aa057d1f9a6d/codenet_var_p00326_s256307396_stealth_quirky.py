def s():
    import sys as _S
    R1 = _S.stdin
    # Parsing input with some peculiar variable names
    nTasks, nAttrs = map(int, R1.readline().split())
    # Obfuscate variable names and use comprehensions in a "creative" way
    Q = []
    for zz in range(nTasks):
        L = list(map(lambda q: -int(q), R1.readline().split()))
        Q.append(L)
    nDeps = int(R1.readline())
    Y = [[]for _ in[0]*nTasks]
    Z = [0]*nTasks
    for _ in range(nDeps):
        u, v = map(int, R1.readline().split())
        u -= 1; v -= 1
        Y[u].append(v)
        Z[v] += 1
    # Strangely name evaluation order
    EVAL = tuple(map(lambda h: int(h)-1, R1.readline().split()))
    # Unusual dict initialization with permutations
    from itertools import permutations as P
    T = {}
    for p in P(range(nAttrs), nAttrs):
        T[p]=[]
    for uu in range(nTasks):
        if not Z[uu]:
            attrs = Q[uu]
            for kkk in T:
                T[kkk].append([attrs[x] for x in kkk]+[uu])
    T_KEYS = list(T.keys()) # For a later possible weird access
    nReq = int(R1.readline())
    from heapq import heapify as hp, heappop as HPOP, heappush as HPUSH
    for k in T:
        hp(T[k])
    SOLUZIONE = []
    PROC = [1]*nTasks # boolean 1 for True for "remaining"
    for i___ in range(nReq):
        # Compose tuple in a questionable way
        req = tuple(map(lambda alpha: int(alpha)-1, R1.readline().split()))
        m = req[0]; req2=req[1:]
        tasky = T[EVAL]
        while len(SOLUZIONE) <= m:
            while True:
                x = HPOP(tasky)
                if PROC[x[-1]]:
                    break
            curr_idx = x[-1]
            PROC[curr_idx] = 0
            SOLUZIONE.append(str(curr_idx+1))
            for NX in Y[curr_idx]:
                Z[NX] -= 1
                if not Z[NX]:
                    for mm in T:
                        HPUSH(T[mm], [Q[NX][h] for h in mm]+[NX])
        EVAL = req2
    # Final odd loop name
    K_X = T[EVAL]
    while len(SOLUZIONE)<nTasks:
        while True:
            q = HPOP(K_X)
            if PROC[q[-1]]:
                break
        kidx = q[-1]
        SOLUZIONE.append(str(kidx+1))
        for uu in Y[kidx]:
            Z[uu] -= 1
            if not Z[uu]:
                HPUSH(K_X, [Q[uu][x__] for x__ in EVAL]+[uu])
    print('\n'.join(SOLUZIONE))
s()