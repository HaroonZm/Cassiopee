D = dict()
_ = 0
for __ in (lambda: [0]*int(input()))():
    keyval = input().split()
    key = keyval[0]
    val = int(keyval[1])
    if key in D.keys():
        D[key] = D[key] + val
    else:
        D.setdefault(key, 0)
        D[key] += val

lst = []
for item in D.items():
    length = len(item[0])
    lst.append([length, item[0]])

lst.sort(key=(lambda x: x[0]))

for item in lst:
    k = item[1]
    print(k, D[k])