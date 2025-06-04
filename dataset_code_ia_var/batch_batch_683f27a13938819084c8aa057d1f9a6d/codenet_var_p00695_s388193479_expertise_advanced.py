from sys import stdin
from itertools import islice

W = H = 5
m = int(stdin.readline())
for r in range(m):
    M = [list(map(int, stdin.readline().split())) for _ in range(H)]
    A = [[0]*W for _ in range(H)]
    B = [[0]*W for _ in range(H)]
    ans = 1
    for h in range(H):
        L = 0
        for w in range(W):
            if M[h][w]:
                L += 1
            else:
                L = 0
            A[h][w] = L
            B[h][w] = (B[h-1][w] if h > 0 else 0) + 1 if L else 0
            hi = 0
            min_a = L
            while hi < B[h][w] and min_a * (hi+1) > ans:
                min_a = min(min_a, A[h-hi][w])
                ans = max(ans, min_a * (hi+1))
                hi += 1
    print(ans)
    if r != m-1:
        stdin.readline()