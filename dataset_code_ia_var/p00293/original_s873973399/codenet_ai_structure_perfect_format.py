t = set([])
a = map(int, raw_input().split())
n = a[0]
for i in xrange(n):
    t.add(a[2 * i + 1] * 60 + a[2 * i + 2])
b = map(int, raw_input().split())
n = b[0]
for i in xrange(n):
    t.add(b[2 * i + 1] * 60 + b[2 * i + 2])
tl = list(t)
tl.sort()
print " ".join(":".join([str(time // 60), str(time % 60).zfill(2)]) for time in tl)