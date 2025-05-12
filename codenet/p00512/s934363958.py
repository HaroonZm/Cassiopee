n = int(input())
o = {}
for i in range(n):
    name, value = input().split()
    if name in o:
        o[name] += int(value)
    else:
        o[name] = int(value)
o = sorted(o.items(), key=lambda x: x[0])
o.sort(key = lambda x: len(x[0]))
for i in o:
    print("{0} {1}".format(i[0], i[1]))