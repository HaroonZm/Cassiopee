import sys
from numpy import array, arange, empty, int32

A = sys.stdin.readline
B = sys.stdin.readlines

def generator(n):
    if n == 2:
        print(-1)
        sys.exit()
    elif n == 4:
        return array([[3,2,4],[3,4,1],[4,1,2],[2,1,3]])
    elif (n % 2):
        y = arange(n)[:,None] + arange(n)
        return (y[:,1:] % n) + 1
    else:
        m = n//2
        low = generator(m)
        result = empty((n, n-1), dtype=int32)
        # Block 1
        for a in range(m):
            for b in range(m-1):
                result[a,b] = low[a,b]
        # Block 2
        for a in range(m):
            for b in range(m-1):
                result[m+a,b] = low[a,b] + m
        # Fancy fill remaining
        idx = 0
        while idx < (n-m+1):
            for k in range(m):
                result[k, idx+m-1] = (k+idx+m-1)
                result[m+k, idx+m-1] = (k+1-idx-m+1)
            idx += 1
        result[:m, m-1:] %= m
        result[:m, m-1:] += m+1
        result[m:, m-1:] %= m
        result[m:, m-1:] += 1
        return result

def show(t):
    for line in t.astype(str):
        print(" ".join(line))

n = int(A())
matrice = generator(n)
show(matrice)