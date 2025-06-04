import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x + "\n")

h, w, a, b = map(int, input().split())

M = 10**9 + 7
N = h + w + 10

g1 = [None] * (N + 1)
g2 = [None] * (N + 1)
inverse = [None] * (N + 1)
g1[0] = g1[1] = g2[0] = g2[1] = 1
inverse[0], inverse[1] = 0, 1

for i in range(2, N + 1):
    g1[i] = (g1[i - 1] * i) % M
    inverse[i] = (-inverse[M % i] * (M // i)) % M
    g2[i] = (g2[i - 1] * inverse[i]) % M

def cmb(n, r, M):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return (g1[n] * g2[r] * g2[n - r]) % M

ans = 0
for i in range(h - a - 1):
    ans += cmb(b + i, i, M) * cmb(w - b - 2 + h - 1 - i, w - b - 2, M)
    ans %= M
i = h - a - 1
ans += cmb(b + i, i, M) * cmb(w - b - 1 + a, a, M)
print(ans % M)