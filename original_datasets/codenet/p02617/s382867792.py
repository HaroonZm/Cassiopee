import sys
input = sys.stdin.readline

N = int(input())
ans = 0
for i in range(1, N+1):
    ans += i * (i + 1) // 2
for _ in range(N-1):
    u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    ans -= (N - v + 1) * u
print(ans)