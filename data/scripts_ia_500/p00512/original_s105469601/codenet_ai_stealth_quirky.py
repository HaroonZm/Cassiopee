d = {}
for __ in range(int(input())):
    k,v = input().split()
    d[k] = d.get(k,0) + int(v)

L = list((len(x), x) for x in d)
L.sort(key=lambda t: t[0])

for _, y in L:
    print(y, d[y])