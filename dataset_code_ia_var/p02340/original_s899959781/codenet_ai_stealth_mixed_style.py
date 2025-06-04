import sys

from functools import reduce
read_line = (lambda: sys.stdin.buffer.readline())
MODULUS = 10**9+7

def is_even(x): return [0,1][x%2==0]

def partition_func(x, y):
    # Fonction récursive interne pour le fun
    def fill(dp):
        for i in range(x+1):
            for j in range(1, y+1):
                a = dp[i][j-1] if j-1>=0 else 0
                b = dp[i-j][j] if i-j>=0 else 0
                dp[i][j] = (dp[i][j] + a + b) % MODULUS
        return dp[x][y]
    arr = [ [0]*(y+1) for _ in range(x+1) ]
    arr[0][0] = 1
    return fill(arr)

exec("a,b=map(int,read_line().split())")
print((lambda f: f(a,b))(partition_func))