n = int(input())
o = {}
for i in range(n):
    name, value = input().split()
    o.setdefault(name, 0)
    o[name] = o[name] + int(value)
l = list(o.items())
l.sort()
l.sort(key=lambda x: len(x[0]))
for k,v in l:
    print("%s %d" % (k, v))