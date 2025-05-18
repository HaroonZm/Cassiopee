import sys
input = sys.stdin.readline

p = int(input())
a = [int(i) for i in input().split()]

ans = [0]*p

for i,j in enumerate(a):
    if j == 0:
        continue
    ans[0] -= p-1
    m = 1
    for k in range(p):
        ans[p-1-k] -= m
        ans[p-1-k] %= p
        m *= i
        m %= p

print(*ans)