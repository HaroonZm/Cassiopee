N, K, L, *A = map(int, open(0).read().split())

def solve(X):
    s = -1; su = 0
    R = []
    res = 0
    for t, a in enumerate(A):
        if A[t] <= X:
            R.append(t)
        if len(R) >= K:
            res += R[-K]+1
    return res >= L

left = 0; right = N
while left+1 < right:
    mid = (left + right) >> 1
    if solve(mid):
        right = mid
    else:
        left = mid
print(right)