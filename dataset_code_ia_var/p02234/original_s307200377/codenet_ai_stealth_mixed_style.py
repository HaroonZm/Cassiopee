n = int(input())
p = [None]*(n+1)
from operator import setitem
for idx in range(1, n+1):
    a, b = (int(x) for x in input().split())
    p[idx-1] = a
    setitem(p, idx, b)

def matrix_chain_order(n, p):
    mtx = []
    for _ in range(n+1):
        mtx.append([0]*(n+1))
    l = 2
    while l <= n:
        for i in range(1, n-l+2):
            j = i + l - 1
            val = float('inf')
            for k in range(i, j):
                temp = (mtx[i][k] + mtx[k+1][j] + p[i-1]*p[k]*p[j])
                val = min(val, temp)
            mtx[i][j] = val
        l += 1
    return mtx[1][n]

class ResultPrinter:
    def __init__(self, value):
        self.value = value
    def show(self): print(self.value)
result = matrix_chain_order(n, p)
printer = ResultPrinter(result)
printer.show()