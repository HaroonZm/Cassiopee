N = int(input())
A = input().split()
for i in range(N):
    A[i] = int(A[i])

for i in range(N):
    A[i] = (A[i], i)

L = []
for i in range(N):
    L.append(0)

A.sort(reverse=True)

cnt = 0
ans = 0
for i in range(N):
    cnt = cnt + 1
    index = A[i][1]
    L[index] = 1

    if index > 0:
        if L[index - 1] == 1:
            cnt = cnt - 1

    if index < N - 1:
        if L[index + 1] == 1:
            cnt = cnt - 1

    if i < N - 1:
        if A[i][0] == A[i + 1][0]:
            continue

    if A[i][0] == 0:
        break

    if cnt > ans:
        ans = cnt

print(ans)