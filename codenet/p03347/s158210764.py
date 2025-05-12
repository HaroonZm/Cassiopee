N = int(input())
A = [0] * N
for i in range(N):
    A[i] = int(input())

possible = 1
if A[0] != 0:
    possible = 0
ans = 0
for i in range(1, N):
    d = A[i] - A[i-1]
    if d > 1:
        if A[i] != 0:
            possible = 0
            break
    elif d == 1:
        ans += 1
    else:
        ans += A[i]
if possible:
    print(ans)
else:
    print(-1)