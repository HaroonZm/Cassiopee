N = int(input())
A = []
for i in range(N):
    x = int(input())
    A.append(x)
A.sort()

if N % 2 == 0:
    K = N // 2
    ans = 0
    for i in range(K):
        diff = A[i+K] - A[i]
        ans = ans + 2 * diff
    ans = ans + (A[K-1] - A[K])
    print(ans)
else:
    K = (N - 1) // 2
    ans1 = 0
    ans2 = 0
    for i in range(K):
        ans1 = ans1 - 2 * A[i]
        ans2 = ans2 + 2 * A[i + K + 1]
    for i in range(K + 1):
        ans1 = ans1 + 2 * A[i + K]
        ans2 = ans2 - 2 * A[i]
    ans1 = ans1 - (A[K] + A[K + 1])
    ans2 = ans2 + (A[K] + A[K - 1])
    if ans1 > ans2:
        print(ans1)
    else:
        print(ans2)