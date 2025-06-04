import sys
input = sys.stdin.readline

M, N = map(int, input().split())
A = list(map(int, input().split()))

if M == 2:
    ans0 = 0
    ans1 = 0
    for i in range(N):
        if A[i] % 2 == i % 2:
            ans0 += 1
        else:
            ans1 += 1
    print(min(ans0, ans1))
else:
    A.append(10**10)
    count = 1
    ans = 0
    for i in range(1, N + 1):
        if A[i] == A[i - 1]:
            count += 1
        else:
            ans += count // 2
            count = 1
    print(ans)