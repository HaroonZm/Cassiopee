n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

if not any(ti == ai == t[-1] == a[0] for ti, ai in zip(t, a)):
    print(0)
    exit()

ans = 1
for i in range(1, n - 1):
    if t[i - 1] == t[i] and a[i] == a[i + 1]:
        ans = ans * min(t[i], a[i]) % mod
print(ans)