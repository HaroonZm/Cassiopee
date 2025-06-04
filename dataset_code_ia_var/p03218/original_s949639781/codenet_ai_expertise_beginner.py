mod = 998244353

N = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 1
for i in range(N):
    def get_gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    g = get_gcd(i, a[i])
    ans = (ans * g) % mod

print(ans)