import sys

input = sys.stdin.readline

N = int(input())
D_X = input().split()
D = int(D_X[0])
X = int(D_X[1])
A = []
for i in range(N):
    A.append(int(input()))

ans = X
for a in A:
    cnt = 0
    day = 1
    while day <= D:
        cnt += 1
        day += a
    ans += cnt

print(ans)