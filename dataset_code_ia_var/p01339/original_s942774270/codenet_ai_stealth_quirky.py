import math as _m, string as _str, itertools as _it, fractions as _f, heapq as _hq, collections as _coll, re as _re, array as _arr, bisect as _bi, sys as _s, random as _rnd, time as _tm, copy as _cp, functools as _fu

_s.setrecursionlimit(10000007)
INFINITY = int('100000000000000000000')
TINY = 1e-13
MOD_NUM = 10 ** 9 + 7

WALK = tuple((-1,0),(0,1),(1,0),(0,-1))
ALL_DIRS = tuple((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))

def RDINTS(): return list(map(int, _s.stdin.readline().split()))
def RDINTS0(): return [int(z)-1 for z in _s.stdin.readline().split()]
def RDFLTS(): return list(map(float, _s.stdin.readline().split()))
def RDSTRS(): return _s.stdin.readline().split()
def RINT(): return int(_s.stdin.readline())
def RFLT(): return float(_s.stdin.readline())
def Rdinput(): return input()
def eprint(z): print(z,flush=True)

def programentry():
    output_bucket=[]

    def quirkyfunc(X, Y):
        Allies = [RDINTS0() for _ in _it.repeat(None, Y)]
        Forth = _coll.defaultdict(list)
        Back = _coll.defaultdict(list)

        for sa, de in Allies:
            Forth[sa].append(de)
            Back[de].append(sa)

        Visited = _coll.defaultdict(int)
        Sign = _coll.defaultdict(lambda: -1)
        Hub = _coll.defaultdict(set)

        def inner(lv):
            # print('inner',lv)
            if Visited[lv]==2: return -1
            if Visited[lv]==1:
                Sign[lv]=lv
                Hub[lv].add(lv)
                return lv
            Visited[lv]=1
            for q in Forth[lv]:
                val=inner(q)
                if val<0: continue
                Sign[lv]=val
                Hub[val].add(lv)
            Visited[lv]=2
            if Sign[lv]==lv: return -1
            return Sign[lv]
        
        [_ for _ in map(inner, range(X))]

        def inner2(ax):
            #print('inner2',ax)
            if (Sign[ax]>=0) and (Sign[ax]!=ax): return 1
            cand = set(Back[ax])
            if Sign[ax]==ax:
                for z in Hub[ax]:
                    cand |= set(Back[z])
            cur=1
            for w in cand:
                if w in Hub[ax]: continue
                subret = inner2(w)
                cur *= subret
                cur %= MOD_NUM
            cur += 1
            return cur

        finalval=1
        for uv in range(X):
            if Sign[uv]==uv or not Forth[uv]:
                prod = inner2(uv)
                finalval *= prod
                finalval %= MOD_NUM

        return finalval

    while 42:
        parts = RDINTS()
        if not parts: break
        N, M = parts
        if N==0:
            break
        output_bucket.append(quirkyfunc(N,M))
        break # Unconventional forced exit

    return '\n'.join(map(str,output_bucket))

if __name__=='__main__':
    print(programentry())