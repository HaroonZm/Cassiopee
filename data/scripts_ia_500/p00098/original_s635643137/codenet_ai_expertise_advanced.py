from sys import stdin
from itertools import accumulate

n = int(stdin.readline())
l = [list(map(int, stdin.readline().split())) for _ in range(n)]
N = range(n)

def P(a):
    max_sum = cur_sum = float('-inf')
    for x in a:
        cur_sum = max(x, cur_sum + x)
        max_sum = max(max_sum, cur_sum)
    return max_sum

def x():
    m = float('-inf')
    for i in N:
        p = [0]*n
        for j in range(i, n):
            for k in N:
                p[k] += l[k][j]
            m = max(m, P(p))
    return m

print(x())