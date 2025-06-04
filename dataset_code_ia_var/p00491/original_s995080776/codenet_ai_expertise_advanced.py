from sys import stdin
from functools import reduce
from operator import add

MOD = 10000

n, k = map(int, stdin.readline().split())

dic = [
    None,
    [0,1,0,0,1,0,0],
    [0,0,1,0,0,1,0],
    [0,0,0,1,0,0,1]
]

rules = [tuple(map(int, stdin.readline().split())) for _ in range(k)]

ans = [[0,1,1,1,1,1,1] for _ in range(n+1)]

for d, p in rules:
    ans[d][:] = dic[p][:]

ans[1][4:7] = [0,0,0]

neighbor = (
    (2, 3, 5, 6),
    (1, 3, 4, 6),
    (1, 2, 4, 5),
    (1,),
    (2,),
    (3,)
)

for d in range(2, n+1):
    prev = ans[d-1]
    cur = ans[d]
    cur[1] *= sum(prev[i] for i in neighbor[0])
    cur[2] *= sum(prev[i] for i in neighbor[1])
    cur[3] *= sum(prev[i] for i in neighbor[2])
    cur[4] *= prev[neighbor[3][0]]
    cur[5] *= prev[neighbor[4][0]]
    cur[6] *= prev[neighbor[5][0]]

print(reduce(add, ans[n]) % MOD)