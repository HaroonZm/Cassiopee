N = int(input())
A = [int(a) for a in input().split()]

for i in range(N):
    A[i] = (A[i], i)

L = [0]*N
A.sort(reverse=True)
cnt = 0
ans = 0
for i in range(N):
    cnt += 1
    L[A[i][1]] = 1
    if A[i][1] > 0 and L[A[i][1]-1] == 1:
        cnt -= 1
    if A[i][1] < N-1 and L[A[i][1]+1] == 1:
        cnt -= 1

    if i < N-1 and A[i][0] == A[i+1][0]:
        continue
    if A[i][0] == 0:
        break
    ans = max(ans, cnt)

print(ans)