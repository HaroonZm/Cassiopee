import sys
N, M, p = map(int, sys.stdin.readline().split())
ls = []
for _ in range(M):
    x = int(sys.stdin.readline())
    ls.append((x - p) % N)
ls.sort()
ans = min(ls[-1], N - ls[0])
for i in range(M - 1):
    len1 = ls[i]
    len2 = N - ls[i + 1]
    a = len1 * 2 + len2
    b = len2 * 2 + len1
    if a < ans:
        ans = a
    if b < ans:
        ans = b
print(ans * 100)