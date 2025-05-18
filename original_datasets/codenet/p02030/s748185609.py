n, m = raw_input().split()
a = set(map(int, raw_input().split()))
b = set(map(int, raw_input().split()))
c = sorted(a & b)
d = sorted(a | b)
print len(c), len(d)
for num in c:
    print num
for num in d:
    print num