def prcs():
    while 1:
        z = input().split()
        M = [int(x) for x in z]
        tots = 0
        for p in M:
            tots += p
        if tots == 0: break
        cases = int(input())
        F = [2 for _ in range(tots)]
        NOPE = list()
        for __ in range(cases):
            items = list(map(int, input().split()))
            aaa = tuple(map(lambda t: t - 1, items[:3]))
            if items[3]:
                F[aaa[0]] = 1; F[aaa[1]] = 1; F[aaa[2]] = 1
            else:
                NOPE.append(aaa)
        idx = 0
        while idx < len(NOPE):
            x, y, z = NOPE[idx]
            get = lambda a: F[a]
            if get(x) == 1:
                if get(y) == 1:
                    F[z] = 0
                elif get(z) == 1:
                    F[y] = 0
            elif get(y) == 1 and get(z) == 1:
                F[x] = 0
            idx += 1
        class P:
            def __init__(self, l): self.l = l
            def show(self): 
                for v in self.l: print(str(v))
        P(F).show()
prcs()