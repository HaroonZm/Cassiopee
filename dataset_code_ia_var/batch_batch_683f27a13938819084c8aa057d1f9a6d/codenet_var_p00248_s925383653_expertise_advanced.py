from sys import stdin

def process():
    while True:
        try:
            n, m = map(int, next(stdin).split())
        except StopIteration:
            break
        if n == 0:
            break

        from collections import defaultdict, deque

        D = [deque() for _ in range(n + 1)]
        D[0].extend(range(1, n + 1))
        nflg = False

        for _ in range(m):
            u, v = map(int, next(stdin).split())
            D[u].append(v)
            D[v].append(u)
            if len(D[u]) > 2 or len(D[v]) > 2:
                nflg = True
        if nflg:
            print('no')
            continue

        bkf = False
        while D[0]:
            st = D[0].pop()
            if len(D[st]) == 2:
                D[0].append(st)
                continue
            st0 = st
            while D[st]:
                nxt = D[st].pop()
                if nxt != st0:
                    if nxt in D[0]:
                        D[0].remove(nxt)
                    if st in D[nxt]:
                        D[nxt].remove(st)
                    st = nxt
                else:
                    print('no')
                    bkf = True
                    break
            if bkf:
                break
        else:
            print('yes')

process()