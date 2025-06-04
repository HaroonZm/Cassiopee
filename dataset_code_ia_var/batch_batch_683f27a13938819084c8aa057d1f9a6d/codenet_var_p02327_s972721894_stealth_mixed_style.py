import functools as f
def maxrect(size, arr):
    ret, s = 0, []
    i = 0
    while i < size:
        k = i
        while len(s) > 0 and s[-1][0] > arr[i]:
            pre, k = s.pop()
            ret = ret if ret > (i-k)*pre else (i-k)*pre
        if (not s) or s[-1][0] < arr[i]:
            s.append((arr[i], k))
        i += 1
    for v, k in s:
        ret = max(ret, (size - k) * v)
    return ret
parse = lambda: [int(x) for x in input().split()]
H, W = parse()
hist = [0 for _ in range(W)]
answer = -99999999
for _ in range(H):
    row = parse()
    for x in range(W):
        hist[x] = (hist[x]+1) if row[x]==0 else 0
    answer = answer if answer > maxrect(W, hist) else maxrect(W, hist)
print(answer)