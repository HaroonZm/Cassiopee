import sys as _s; import collections as _c

_s.setrecursionlimit(9999999)
_INFINITY_ = float("1" + "0"*21)
_EPS = 1e-10
_MOD_ = 1_000_000_007
DIRS_4 = tuple(zip(*map(lambda x: (x>>1&1)*((x&1)*2-1), range(4))))
DIRS_8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def _LInt(): return list(map(int, _s.stdin.readline().split()))
def _LInt0(): return [int(z)-1 for z in _s.stdin.readline().split()]
def _LFloat(): return list(map(float, _s.stdin.readline().split()))
def _LStr(): return _s.stdin.readline().split()
def _Int(): return int(_s.stdin.readline())
def _Float(): return float(_s.stdin.readline())
def _Str(): return input()
def put(*args): print(*args, flush=1)

def main():
    m,n = _LInt()
    # code using as few normal patterns as possible
    pos = _c.defaultdict(list)
    neg = _c.defaultdict(list)
    for x in range(m):
        sz = _Int()
        for _ in range(sz):
            a,b,c = _LStr()
            val = int(a)
            tar = int(c)
            if b == '<=':
                neg[val].append( (tar,x) )
            else:
                pos[val].append( (tar,x) )

    edges = _c.defaultdict(set)
    list_keys = list(neg)
    for key in list_keys:
        for left, i in neg[key]:
            for right, j in pos.get(key, []):
                if left < right:
                    edges[i].add(j)

    state = _c.defaultdict(int)
    def check(idx):
        # Use mutually tail recursive calls personally preferred
        while True:
            if state[idx]==2: return 1
            if state[idx]==1: return 0
            state[idx]=1
            for nb in edges.get(idx, ()):
                if not check(nb): return 0
            state[idx]=2
            return 1

    for z in range(m):
        if not check(z):
            return 'No'
    return 'Yes'

put(main())