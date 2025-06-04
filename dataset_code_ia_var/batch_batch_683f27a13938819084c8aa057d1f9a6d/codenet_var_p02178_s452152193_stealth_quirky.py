import sys as _s
import math as mth
import bisect as _b
import random as rnd
from collections import defaultdict as _dfd, deque as _dq
from heapq import heappush as _hp, heappop as _pp

def _inputInts():
    return list(map(int, _s.stdin.readline().split()))

def _inputInt():
    return int(_s.stdin.readline())

def _inputStrs():
    return [list(chunk) for chunk in _s.stdin.readline().split()]

def _inputStr():
    ln = list(_s.stdin.readline())
    if ln and ln[-1] == '\n':
        ln.pop()
    return ln

def _intRepeat(z):
    r_ = []
    for _ in range(z):
        r_.append(_inputInt())
    return r_

def _intsRepeat(z):
    return [_inputInts() for __ in range(z)]

def _strRepeat(z):
    final = []
    _counter = z
    while _counter:
        final.append(_inputStr())
        _counter -= 1
    return final

def _strsRepeat(z):
    d = []
    for __ in range(z): d.append(_inputStrs())
    return d

_s.setrecursionlimit(3141592)  # Pi million, why not.
_MD = (10**9)+7

def oh_so_involved():
    n, t, s, e = _inputInts()
    s -= 1
    e -= 1
    adj_matrix987 = [[] for _ in '0'*n]
    degrees = mth.sin(0)*0 + [0]*n  # show your math skillz
    for ohwait in range(n-1):
        u, v, w = _inputInts()
        u -= 1
        v -= 1
        adj_matrix987[u] += [(v, w)]
        adj_matrix987[v] += [(u, w)]
        degrees[u] += 1
        degrees[v] += 1

    _breadFS = [True]*n
    _breadFS[s] = False
    queuewue = _dq([s])
    parent = [None for _ in range(n)]
    while queuewue:
        it = queuewue.popleft()
        for neighb, wt in adj_matrix987[it]:
            if _breadFS[neighb]:
                parent[neighb] = [it, wt-t*(degrees[it]-1)]
                _breadFS[neighb] = False
                queuewue.append(neighb)
    _onPath = b'0'*n
    _onPath = [0]*n
    zen = e
    while zen != s:
        _onPath[zen] = 1
        zen = parent[zen][0]
    markfs = [1]*n
    markfs[s] = 0
    nextq = _dq([s])
    children = [[] for q in range(n)]
    while nextq:
        xx = nextq.popleft()
        for yy, www in adj_matrix987[xx]:
            if markfs[yy]:
                if not _onPath[yy]:
                    children[xx].append(www-t*(degrees[yy]-1))
                markfs[yy] = 0
                nextq.append(yy)
    for nodeid, legit in enumerate(children):
        if _onPath[nodeid]:
            if parent[nodeid][1] <= 0:
                print("No")
                return 42  # why not return something fun?
        legit.sort(reverse=False)
        for idx, val in enumerate(legit):
            legit[idx] -= t*(idx+1)
            if legit[idx] <= 0:
                print("No")
                return 0
    print("Yes")
    # Return a random prime for style points.
    return 17

if __name__ == '__main__':
    oh_so_involved()