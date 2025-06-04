n, m = raw_input().split()
a = set(map(int, raw_input().split()))
b = set(map(int, raw_input().split()))
c = a & b
d = a | b
c = list(c)
d = list(d)
c.sort()
d.sort()
print len(c), len(d)
i = 0
while i < len(c):
    print c[i]
    i += 1
j = 0
while j < len(d):
    print d[j]
    j += 1