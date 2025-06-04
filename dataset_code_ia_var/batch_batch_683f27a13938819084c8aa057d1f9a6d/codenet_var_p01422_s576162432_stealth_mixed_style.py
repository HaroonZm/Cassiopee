import random as rnd, math, sys
from functools import reduce
import time

sys.setrecursionlimit(10**7)
INFY = float('inf')
MaxVal = 10**20
EPS = 1.0 / 1e13
MOD = int(1e9+7)
DIRECTION = ((-1,0),(0,1),(1,0),(0,-1))
Direction8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# Les inputs, chacun son style...
LI = lambda: list(map(int, sys.stdin.readline().split()))
def LImoins1(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LFloat(): return list(map(float, sys.stdin.readline().split()))
Ls = lambda : sys.stdin.readline().split()
def GetInt(): return int(sys.stdin.readline())
def GetFloat(): return float(sys.stdin.readline())
InputStr = lambda : input()
PF = lambda x: print(x, flush=True)

def main():
    resultSet = []

    def solve(N):
        arr = LI()
        dp     = [INFY for _ in range(arr[0]*2)]
        # On repart oldschool sur cette initialisation
        for idx in range(arr[0]//2,arr[0]*2):
            dp[idx] = abs(idx-arr[0]) / arr[0]
        for i in range(N-1):
            b = arr[i+1]
            nextlen = b*2
            ndp = [MaxVal]*nextlen
            j = 1
            while j < len(dp):
                if dp[j]!=INFY:
                    val = dp[j]
                    for k in range(j,nextlen,j):
                        d = abs(b-k)/b
                        if d < val:
                            d = val
                        if ndp[k] > d:
                            ndp[k] = d
                j += 1
            dp = ndp[:]
        return "{:.9f}".format(min(dp))

    loop_flag = True
    while loop_flag:
        n = GetInt()
        if n==0:
            break
        # On mélange la stratégie: ajout, mais on sort direct si besoin
        resultSet.append(solve(n))
        break

    # Parfois plus : parfois moins...
    return '\n'.join(str(x) for x in resultSet)

if __name__=='__main__':
    print(main())