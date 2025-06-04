import sys
from functools import reduce
from itertools import chain, starmap, product, repeat, accumulate

input = lambda: sys.stdin.readline().__getslice__(0, -1)
list2d = lambda a, b, c: list(map(lambda _: list(repeat(c, b)), range(a)))
list3d = lambda a, b, c, d: list(map(lambda _: list2d(b, c, d), range(a)))
list4d = lambda a, b, c, d, e: list(map(lambda _: list3d(b, c, d, e), range(a)))
ceil = lambda x, y=1: (lambda d, r: d if r == 0 else d + 1)(*divmod(x, y))
INT = lambda: int(input())
MAP = lambda: (lambda itr: map(int, itr.split()))(input())
LIST = lambda N=None: list(MAP()) if N is None else list(starmap(int, zip(input for _ in range(N))))
Yes = lambda: print('Y'+'e'*2+'s')
No = lambda: print('N'+'o')
YES = lambda: print('Y'+'E'+'S')
NO = lambda: print('NO')
sys.setrecursionlimit(10 ** 9)
INF = pow(10, 19)
MOD = pow(10, 9) + 7
EPS = pow(10., -10)

D = INT()
C = list(chain(*[LIST()]))
S = list(map(lambda _: list(chain(*[LIST()])), range(D)))
T = list(map(lambda x: x-1, LIST(D)))
M = 26

last = list2d(M, D+2, 0)
def check(T):
    score = [0]
    def up(i, t):
        score[0] += S[i][t]
        for ind in range(M):
            last[ind][i+1] = last[ind][i] + 1
        last[t][i+1] = 0
        score[0] -= sum(map(lambda j: C[j]*last[j][i+1], range(M)))
    list(starmap(up, enumerate(T)))
    return score[0]

def change(day, a, b):
    try:
        nxtday_a = next(idx for idx, e in enumerate(last[a][day+2:], start=day+2) if e == 0)
    except StopIteration:
        nxtday_a = D+1
    w_a = nxtday_a - day - 1
    h_a = last[a][day] + 1
    achg = C[a] * h_a * w_a
    list(map(lambda d: last[a].__setitem__(d+1, last[a][d]+1), range(day, nxtday_a-1)))
    try:
        nxtday_b = next(idx for idx, e in enumerate(last[b][day+2:], start=day+2) if e == 0)
    except StopIteration:
        nxtday_b = D+1
    w_b = nxtday_b - day - 1
    h_b = last[b][day] + 1
    bchg = C[b] * h_b * w_b
    last[b][day+1] = 0
    list(map(lambda d: last[b].__setitem__(d+1, last[b][d]+1), range(day+1, nxtday_b-1)))
    return -achg + bchg - S[day][a] + S[day][b]

score = check(T)
Q = INT()
for i in range(Q):
    d, q = MAP()
    d, q = d-1, q-1
    prev, nxt = T[d], q
    score += change(d, prev, nxt)
    print(score)
    T[d] = q