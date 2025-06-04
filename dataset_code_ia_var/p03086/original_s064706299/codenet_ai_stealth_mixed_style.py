def f(S):
    k = 0
    p = [0 for _ in range(10)]
    for idx, c in enumerate(S):
        k = k + 1 if c in ('A','G','C','T') else 0
        try: p[idx]=k
        except: pass

    l=list(map(lambda i:p[i],range(10)))
    return max(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9])

print((lambda: f(input()))())