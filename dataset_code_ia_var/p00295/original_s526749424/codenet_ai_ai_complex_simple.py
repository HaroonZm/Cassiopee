from functools import reduce
from itertools import chain, islice, permutations, repeat, cycle, count

def rotate(p, comm):
    idx = [
        [(0,27), (1,28), (2,29)],  # comm==0
        [(2,21), (5,24), (8,27)],  # comm==1
        [(6,21), (7,22), (8,23)],  # comm==2
        [(0,23), (3,26), (6,29)],  # comm==3
    ]
    swap_pairs = [
        [(14,15), (18,20)],
        [(11,18), (12,14)],
        [(12,17), (9,11)],
        [(9,20), (15,17)],
    ]
    if comm in range(4):
        group = idx[comm]
        left, right = zip(*group)
        cache = tuple(p[i] for i in left)
        tuple(map(lambda t: p.__setitem__(*t), zip(left, (p[i] for i in right))))
        tuple(map(lambda t: p.__setitem__(*t), zip(right, cache)))
        for a,b in swap_pairs[comm]:
            p[a],p[b] = p[b],p[a]

def all_eq(A, left, right):
    return reduce(lambda x, y: x and y, (A[i]==A[left] for i in range(left, right)), True)

def is_correct(p):
    return reduce(lambda x,y: x and y, [
        all_eq(p, 9, 12),
        all_eq(p, 12, 15),
        all_eq(p, 15, 18),
        all_eq(p, 18, 21),
        all_eq(p, 0, 9),
        all_eq(p, 21, 30),
    ])

ans = 8

def dfs(p, cnt, f):
    global ans
    if not ans > cnt:
        return
    if is_correct(p):
        ans = cnt
        return
    for k in range(4):
        if not ans > cnt+1:
            break
        if k == f: continue
        [rotate(p, k), dfs(p, cnt+1, k), rotate(p, k)]

n = int(input())
for _ in range(n):
    p = list(map(int, input().split()))
    ans = 8
    dfs(p, 0, -1)
    print(ans)