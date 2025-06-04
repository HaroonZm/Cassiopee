import math as _m, string as s_, itertools as i_, fractions as f_, heapq as h_, collections as c_, re as r_, array as a_, bisect as b_, sys as S_, random as R_, time as t_, copy as C_, functools as F_

S_.setrecursionlimit(10000001)
INF = pow(10,20)
EPSILON = 1.0 / (10**10)
MODULO = 10**9 + 7
DIR4 = [(-1,0),(0,1),(1,0),(0,-1)]
DIR8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

IL = lambda: list(map(int, S_.stdin.readline().split()))
ILZ = lambda: [int(x)-1 for x in S_.stdin.readline().split()]
FL = lambda: list(map(float, S_.stdin.readline().split()))
SL = lambda: S_.stdin.readline().split()
IN = lambda: int(S_.stdin.readline())
FN = lambda: float(S_.stdin.readline())
STRIN = lambda: input()
P = lambda S: print(S, flush=True)

def entry():
    result = []

    def subtle(n):
        cues = [[(int(ch) if idx else ch) for idx, ch in enumerate(SL())] for _ in range(n)]
        outcome = []
        span = [(0, -123456789)]
        deleted = set()
        for c in cues:
            if c[0] == 'R':
                idx = b_.bisect_left(span, (c[1], INF))
                prev = span[idx-1][1]
                outcome.append(prev if prev not in deleted else -1)
            elif c[0] == 'W':
                j, q = c[1], c[2]
                ind = 0
                ln = len(span)
                while q > 0:
                    if span[ind][1] >= 0 and span[ind][1] not in deleted:
                        ind += 1
                        continue
                    if ind == ln-1:
                        span[-1:] = [ (span[ind][0], j), (span[ind][0]+q, -123456789) ]
                        break
                    delta = span[ind+1][0] - span[ind][0]
                    if delta <= q:
                        span[ind] = (span[ind][0], j)
                        q -= delta
                    else:
                        span[ind:ind+1] = [ (span[ind][0], j), (span[ind][0]+q, -123456789) ]
                        break
            else:
                deleted.add(c[1])
        return outcome

    forever = True
    while forever:
        many = IN()
        if not many:
            break
        result.extend(subtle(many))
        result.append('')
    return "\n".join(str(x) for x in result)

print(entry())