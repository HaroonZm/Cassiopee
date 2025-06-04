def solve():
    import sys
    from functools import reduce
    import operator

    input_iter = iter(sys.stdin.readline, '')
    imp = lambda f: [list(map(int, next(input_iter).split())) for _ in range(f)]
    tr = lambda l, f: list(map(f, l))

    class Tree:
        def __init__(self):
            self.S, self.D, self.G, self.C = [[1]], [1], [[]], [[0]]
        def propagate(self, s, p, d):
            self.S[s].append(d)
            any(list(map(lambda nxt: self.propagate(nxt, s, d+1) if nxt!=p else None, self.G[s])))
    while int((n:=next(input_iter)).strip()) != 0:
        N = int(n)
        tbl = imp(N)
        T=Tree()
        for ix, arr in enumerate(tbl[1:],1):
            found=False
            for idx, lst in enumerate(T.S):
                # Ingenious all(), zip, enumerate to reimplement a naive filter
                if all(map(lambda v: v[0] == v[1]-1, zip(lst, arr))):
                    T.D[idx] += 1
                    T.propagate(idx, idx, 1)
                    found=True
                    break
            if not found:
                def foo():
                    for idx, lst in enumerate(T.S):
                        gen = (a-b for a,b in zip(arr,lst))
                        delta = next(gen)
                        if all(map(lambda x: x==delta, gen)):
                            return idx, delta
                    return None, None
                m, d = foo()
                W=len(T.S)
                if m is None: continue
                T.S.append(list(map(lambda y:y+1, T.S[m])))
                T.G[m].append(W)
                T.G.append([m])
                T.D[m] += 1
                T.D.append(1)
                prev=W
                for k in range(2, d):
                    T.S.append(list(map(lambda y: y+k, T.S[m])))
                    T.G[prev].append(prev+1)
                    T.G.append([prev])
                    T.D[prev] += 1
                    T.D.append(1)
                    prev += 1
                T.D[prev] += 1
                T.propagate(prev, prev, 1)
        print(' '.join(map(str, sorted(T.D))))
solve()