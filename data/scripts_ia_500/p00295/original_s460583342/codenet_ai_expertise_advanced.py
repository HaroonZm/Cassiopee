from functools import lru_cache

def rotate(p, comm):
    swaps = {
        0: ((0, 1, 2, 27, 28, 29), (27, 28, 29, 0, 1, 2), ((14, 15), (18, 20))),
        1: ((2, 5, 8, 21, 24, 27), (21, 24, 27, 2, 5, 8), ((11, 18), (12, 14))),
        2: ((6, 7, 8, 21, 22, 23), (21, 22, 23, 6, 7, 8), ((12, 17), (9, 11))),
        3: ((0, 3, 6, 23, 26, 29), (23, 26, 29, 0, 3, 6), ((9, 20), (15, 17))),
    }

    idx_from, idx_to, pairs = swaps[comm]
    p_temp = p[:]
    for i_from, i_to in zip(idx_from, idx_to):
        p[i_to] = p_temp[i_from]
    for i, j in pairs:
        p[i], p[j] = p[j], p[i]

def all_eq(A, left, right):
    ref = A[left]
    return all(x == ref for x in A[left:right])

def is_correct(p):
    # Faces indices grouped
    faces = [(9, 12), (12, 15), (15, 18), (18, 21), (0, 9), (21, 30)]
    return all(all_eq(p, start, end) for start, end in faces)

ans = 8

def dfs(p, cnt, f):
    global ans
    if ans <= cnt:
        return
    if is_correct(p):
        ans = cnt
        return
    for k in range(4):
        if ans <= cnt + 1:
            break
        if k == f:
            continue
        rotate(p, k)
        dfs(p, cnt + 1, k)
        rotate(p, k)

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    p = list(map(int, input().split()))
    ans = 8
    dfs(p, 0, -1)
    print(ans)