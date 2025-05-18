def solve(A, x):
    i = 0
    total = 0
    res = 0
    for j in range(N):
        total += A[j]
        while total > x:
            total -= A[i]
            i += 1
        res += j - i + 1
    return res

N, Q = map(int, input().split())
A = list(map(int, input().split()))
X = list(map(int, input().split()))

for x in X:
    print(solve(A, x))