from sys import setrecursionlimit
setrecursionlimit(10**7)

rotations = [
    ([0,1,2,27,28,29], [27,28,29,0,1,2], [(14,15), (18,20)]),
    ([2,5,8,21,24,27], [21,24,27,2,5,8], [(11,18), (12,14)]),
    ([6,7,8,21,22,23], [21,22,23,6,7,8], [(12,17), (9,11)]),
    ([0,3,6,23,26,29], [23,26,29,0,3,6], [(9,20), (15,17)])
]

def rotate(p, comm):
    idx_from, idx_to, swaps = rotations[comm]
    p_slice = [p[i] for i in idx_from]
    for i, v in zip(idx_from, idx_to):
        p[i] = p_slice[idx_from.index(v)]
    for i,j in swaps:
        p[i], p[j] = p[j], p[i]

def all_eq(A, start, end):
    val = A[start]
    return all(x == val for x in A[start:end])

def is_correct(p):
    return all(all_eq(p, s, e) for s,e in [(9,12),(12,15),(15,18),(18,21),(0,9),(21,30)])

ans = 8

def dfs(p, cnt, f):
    global ans
    if cnt >= ans:
        return
    if is_correct(p):
        ans = cnt
        return
    for k in range(4):
        if k == f:
            continue
        rotate(p, k)
        dfs(p, cnt+1, k)
        rotate(p, k)  # revert

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    p = list(map(int, input().split()))
    ans = 8
    dfs(p, 0, -1)
    print(ans)