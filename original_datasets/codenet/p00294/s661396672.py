import bisect
n, m, p = map(int, raw_input().split())
d = []
for i in xrange(m):
    inp = int(raw_input())
    d.append((inp - p + n) % n)
d.sort()
ans = min(d[-1], n-d[0])
for i in xrange(m-1):
    ans = min(ans, d[i] + (d[i] + n-d[i+1]))
for i in xrange(m-1):
    ans = min(ans, (n-d[i+1]) + (n-d[i+1] + d[i]))
print ans*100