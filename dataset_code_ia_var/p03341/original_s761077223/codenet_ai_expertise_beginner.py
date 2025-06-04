N = int(input())
S = input()

A = [0] * (N + 1)

for i in range(1, N + 1):
    if S[i - 1] == "W":
        A[i] = A[i - 1] + 1
    else:
        A[i] = A[i - 1]

ans = N
for i in range(1, N + 1):
    val = N - i + A[i] - A[N]
    tmp = A[i - 1] + val
    if tmp < ans:
        ans = tmp

print(ans)