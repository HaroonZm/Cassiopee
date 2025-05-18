import sys

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 19
MOD = 10 ** 9 + 7
EPS = 10 ** -10

D = INT()
C = LIST()
S = [[]] * D
for i in range(D):
    S[i]  = LIST()
T = [t-1 for t in LIST(D)]
M = 26

last = list2d(M, D+2, 0)
def check(T):
    score = 0
    for i, t in enumerate(T):
        score += S[i][t]
        for j in range(M):
            last[j][i+1] = last[j][i] + 1
        last[t][i+1] = 0
        for j in range(M):
            score -= C[j] * last[j][i+1]
    return score

def change(day, a, b):
    nxtday = last[a].index(0, day+2)
    w = nxtday - day - 1
    h = last[a][day] + 1
    a_change = C[a] * h * w
    for d in range(day, nxtday-1):
        last[a][d+1] = last[a][d] + 1

    nxtday = last[b].index(0, day+2)
    w = nxtday - day - 1
    h = last[b][day] + 1
    b_change = C[b] * h * w
    last[b][day+1] = 0
    for d in range(day+1, nxtday-1):
        last[b][d+1] = last[b][d] + 1

    res = -a_change + b_change - S[day][a] + S[day][b]
    return res

score = check(T)
Q = INT()
for i in range(Q):
    d, q = MAP()
    d -= 1; q -= 1

    prev = T[d]
    nxt = q
    score += change(d, prev, nxt)
    print(score)
    T[d] = q