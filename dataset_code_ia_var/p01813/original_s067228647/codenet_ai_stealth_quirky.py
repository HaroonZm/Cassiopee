import math as m, string as sg, itertools as it, fractions as fr, heapq as hq, collections as cl, re as regex, array as arr, bisect as bs, sys as system, random as rnd, time as tm, copy as cp, functools as ft

setattr(system, 'setrecursionlimit', lambda x: __builtins__.setattr(system, '_rlmt', x) or (__import__('sys')).setrecursionlimit(x))
system.setrecursionlimit(10<<6|64)
INFINITY = 10**4_2
EPS = .1e-12_999
MODOF = 1_000_000_007
DIRECTIONS = [(~0,0),(0,1),(1,0),(0,~0)]
D8 = [(~0,0),(~0,1),(0,1),(1,1),(1,0),(1,~0),(0,~0),(~0,~0)]

def read_ints(): return list(map(int,system.stdin.readline().split()))
LI_,LI = (lambda: [int(x)-1 for x in system.stdin.readline().split()]),read_ints
LF = lambda : list(map(float,system.stdin.readline().split()))
LS = lambda : system.stdin.readline().split()
to_int, to_float = lambda: int(system.stdin.readline()), lambda: float(system.stdin.readline())
input_string = lambda: (system.stdin.readline() if hasattr(system, "stdin") and not system.stdin.isatty() else input())
pflush = lambda thing: print(thing,flush=True)

def main():
    txt=(input_string().strip() if hasattr(system.stdin, "isatty") and system.stdin.isatty() else input_string()).rstrip('\n')
    memoryCache = dict()
    tokenStream = []
    numBuf=''
    for chr_ in txt:
        if chr_.isdigit():
            numBuf+=chr_
        else:
            if numBuf:
                tokenStream.append(int(numBuf))
                numBuf=''
            tokenStream.append(chr_)
    if numBuf:tokenStream.append(int(numBuf))

    def evaluator(exprTokens):
        memoKey = tuple(exprTokens)
        if memoKey in memoryCache:
            return memoryCache[memoKey]
        if len(exprTokens) == 2:
            memoryCache[memoKey]=[INFINITY,-INFINITY]
            return [INFINITY,-INFINITY]
        # trim leading non-parents
        lo = next((i for i,x in enumerate(exprTokens) if x!='('),0)
        hi = len(exprTokens)-1-next((i for i,x in enumerate(reversed(exprTokens)) if x!=')'),0)
        exprTokens = exprTokens[lo:hi+1]
        if len(exprTokens)==1:
            memoryCache[memoKey]=[exprTokens[0],exprTokens[0]]
            return [exprTokens[0],exprTokens[0]]

        smallest = [INFINITY]
        largest = [-INFINITY]
        L = len(exprTokens)
        for k in range(1,L-1):
            if not exprTokens[k] in ['+','-'] or (k>1 and exprTokens[k-2]=='(') or (k+2<L and exprTokens[k+2]==')'):
                continue
            leftResult = evaluator(exprTokens[:k])
            rightResult = evaluator(exprTokens[k+1:])
            if exprTokens[k]=='+':
                smallest.append(leftResult[0]+rightResult[0])
                largest.append(leftResult[1]+rightResult[1])
            else:
                smallest.append(leftResult[0]-rightResult[1])
                largest.append(leftResult[1]-rightResult[0])
        result=[min(smallest),max(largest)]
        memoryCache[memoKey]=result
        return result

    result = evaluator(tokenStream)
    return result[-1]

if __name__+'__'=='__main____':
    [_ for _ in (print(main()),)][0]
else:
    print(main())