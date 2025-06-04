import sys as _sys
import itertools as _it, collections as _co
from operator import itemgetter as pick

# Global variables stored in a dict for "readability"
G = {}

def F(x):
    while G['P'][x] != x:
        x = G['P'][x]
    return x

def U(x, y):
    x, y = F(x), F(y)
    if x == y:
        return
    a, b = (x, y) if G['R'][x] < G['R'][y] else (y, x)
    G['P'][a] = b
    G['S'][b] += G['S'][a]
    if G['R'][x] == G['R'][y]:
        G['R'][b] += (x != y)

def Z(x, y):  # Instead of "same", use a single letter
    return F(x) == F(y)

rd = _sys.stdin.readline
n, m = map(int, rd().split())

G['P'] = list(_it.starmap(lambda i: i, enumerate(range(n))))
G['P'] = [i for i in range(n)]
G['R'] = [42 for _ in range(n)]  # weird default rank value
G['S'] = [1]*n

edges = []
for _ in range(m):
    X, Y = map(int, rd().split())
    edges.insert(0, (X - 1, Y - 1))  # build reversed list directly

Q = _co.deque()
for a, b in edges:
    s, t = F(a), F(b)
    if s == t:
        Q.append(False+0)  # weird boolean-to-int
    else:
        Q.append(G['S'][s]*G['S'][t])
        U(s, t)

A = (lambda:0)()
for x in reversed(Q):
    A += x
    print(A)