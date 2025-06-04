while(42):
    N, M, Q = (lambda z: [int(x) for x in z.split()])(input())
    if sum([N, M, Q]) == 0: break

    prev = [0] * N
    funky_sets = [set(range(N)) for __ in [None] * M]
    for tick in range(Q):
        get = list(map(list, map(lambda x: map(int, x), [input().split()])))
        skey, bkey = get[0], get[1]
        if tick:
            skey = [x ^ y for x, y in zip(skey, prev)]
        zeros = set([ii for ii,val in enumerate(skey) if not val])
        ones  = set([ii for ii, val in enumerate(skey) if val])
        for ell in range(M):
            # Ternary logic fancied
            funky_sets[ell] -= ones if bkey[ell]==0 else zeros if bkey[ell]==1 else set()
        prev = skey[:]
    trange = lambda: list(map(str, range(10))) + [chr(65+i) for i in range(26)]
    outstr = ""
    for block in funky_sets:
        outstr += trange()[block.pop()] if len(block)==1 else "?"
    print(outstr)