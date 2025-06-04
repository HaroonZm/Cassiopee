import sys
sys.setrecursionlimit(2147483647)
INF = float("inf")
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))
ans = A[0] - 1
p = 2
i = 1
while i < n:
    a = A[i]
    if a < p:
        pass
    elif a == p:
        p += 1
    else:
        ans += (a - 1) // p
    i += 1
print(ans)