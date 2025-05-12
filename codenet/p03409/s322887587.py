n = int(input())
A = [[int(i) for i in input().split()] for j in range(n)]
C = [[int(i) for i in input().split()] for j in range(n)]

ans = 0
used = [False] * n
A.sort(key=lambda x:x[1], reverse=True)
C.sort()

for c, d in C:
    i = 0
    while i < n and (used[i] or A[i][0] >= c or A[i][1] >= d):
        i += 1
    if i >= n:
        continue
    ans += 1
    used[i] = True

print(ans)