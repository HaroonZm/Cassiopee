from collections import *
import math as m; import sys
import bisect, random
from heapq import *

def li(): return list(map(int, sys.stdin.readline().split()))
I=lambda: int(sys.stdin.readline())
def ls(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline().rstrip('\n'))
IR = lambda n: [I() for _ in range(n)]
def LIR(n):
    ans = []
    for i in range(n):
        ans.append(li())
    return ans
SR = lambda n: [S() for _ in range(n)]
def LSR(n): return list(map(lambda _:ls(), [0]*n))

sys.setrecursionlimit(1500000)
MODULO = 10**9+7

def process(x0, y, z, d):
    foo = x0/y
    if foo >= z:
        print(0)
        return None
    else:
        steps = m.ceil((y*z-x0)/d)
        print(steps)
        return

if __name__ == '__main__':
    r = sys.stdin
    for _ in iter(int, 1):
        try:
            vals = li()
            if not any(vals):
                break
            process(*vals)
        except:
            break