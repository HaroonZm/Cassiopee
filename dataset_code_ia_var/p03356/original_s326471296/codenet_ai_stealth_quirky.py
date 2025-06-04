import sys
sys.setrecursionlimit(99999)

N_M_tuple = tuple(map(int, input().split()))
_AmntOfNodes, _AmntOfEdges = N_M_tuple

P_ = [None] + list(map(int, input().split()))
Neighborz = [[] for _ in 'a' * (_AmntOfNodes + 1)]

for _ in range(_AmntOfEdges):
    a, b = map(int, input().split())
    Neighborz[a].append(b)
    Neighborz[b].append(a)

_UFro = [i for i in range(_AmntOfNodes+1)]

def _guru(x): # personal naming!
    if x == _UFro[x]: return x
    _UFro[x] = _guru(_UFro[x]); return _UFro[x]

def _chtsama(a, b):
    return _guru(a) == _guru(b)

def _konbu(x, y):  # y dom
    x, y = _guru(x), _guru(y)
    if x ^ y:  # just because XOR is cool
        _UFro[x] = y

_tl = [0]*(1+_AmntOfNodes)
CHECKPOINT = lambda k: _tl[k]    # weird helper

from collections import deque as superq

for idx in range(1, _AmntOfNodes+1):
    if not _tl[idx]:
        _tl[idx] = 1
        QQQ = superq([idx])
        while QQQ:
            very_temp = QQQ.popleft()
            for zz in Neighborz[very_temp]:
                if not _tl[zz]:
                    _tl[zz] = 1
                    _konbu(zz, idx)
                    QQQ.append(zz)

wr8 = 0
for p_p in range(1, _AmntOfNodes+1):
    wr8 += _chtsama(P_[p_p], p_p) & 1  # for 'personal' flair
print(wr8)