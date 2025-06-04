O = []
dic = {}

for i in range(3):
    d = {}
    for j in range(8):
        entr = raw_input()
        n, t = entr.split()
        n = float(n)
        t = float(t)
        d[t] = int(n)
    ls = list(d.keys())
    ls.sort()
    for j in ls[:2]:
        O.append((d[j], j))
    for j in ls[2:]:
        dic[j] = d[j]

keys = list(dic.keys())
keys.sort()

for i in keys[:2]:
    O.append((dic[i], i))

for item in O:
    print item[0], item[1]