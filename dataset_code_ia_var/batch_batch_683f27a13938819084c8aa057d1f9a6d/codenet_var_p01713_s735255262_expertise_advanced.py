from sys import stdin

W = int(input())
A = list(map(int, stdin.readline().split()))
L = [0] * W
R = [0] * W

def process(A, W, reverse=False):
    arr = [0] * W
    idx_range = range(W - 1, -1, -1) if reverse else range(W)
    now0, nowx = -1, 10**6
    for i in idx_range:
        idx = i if not reverse else i
        val = A[idx]
        if val == 0:
            now0, nowx = idx, 10**6
        if now0 == -1:
            continue
        nowx -= 1
        if val < 0:
            nowx = min(nowx, -val)
        if val > 0:
            arr[idx] = min(val, nowx)
    return arr

L = process(A, W, reverse=False)
R = process(A, W, reverse=True)
ans = sum(max(l, r) for l, r in zip(L, R) if max(l, r) > 0)
print(ans)