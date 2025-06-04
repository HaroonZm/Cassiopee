import sys
import math

PERMUTATIONS = lambda n, r: math.factorial(n) // math.factorial(n - r)

def compute():
    MOD = 10**9+7
    n_m = (lambda l: (int(l[0]), int(l[1])))(sys.stdin.readline().strip().split())
    def fact(x): return math.factorial(x)
    n, m = n_m
    if n == m:
        y = (fact(n)%MOD)*(fact(m)%MOD)
        res = (y*2)%MOD
        print(res)
        return None
    if abs(n-m)==1:
        z = (fact(n)%MOD)*(fact(m)%MOD)
        print(z%MOD)
        return
    [print(0)]

if __name__=='__main__':
    compute()