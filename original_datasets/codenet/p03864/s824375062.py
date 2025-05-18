n, x = map(int, raw_input().split())
a = map(int, raw_input().split())
ans = 0
for i in xrange(n - 1):
    o = a[i] + a[i + 1] - x
    if o > 0:
        ans += o
        a[i + 1] -= min(o, a[i + 1])

print ans