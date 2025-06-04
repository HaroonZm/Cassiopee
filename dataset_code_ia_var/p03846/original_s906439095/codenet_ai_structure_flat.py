N = int(input())
mod = 10 ** 9 + 7
A = list(map(int, input().split()))
B = [0] * N
i = 0
while i < N:
    B[A[i]] += 1
    i += 1
f = 0
if N % 2 == 0:
    ans = 1
    i = 1
    while i < N:
        if B[i] != 2:
            f = 1
            break
        ans = (ans * 2) % mod
        i += 2
    if f == 1:
        print(0)
    else:
        print(ans)
else:
    ans = 1
    if B[0] != 1:
        f = 1
    i = 2
    while i <= N and f == 0:
        if B[i] != 2:
            f = 1
            break
        ans = (ans * 2) % mod
        i += 2
    if f == 1:
        print(0)
    else:
        print(ans)