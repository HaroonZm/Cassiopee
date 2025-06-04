d = input().split()
a = input().split()
p = [(-1, 2, 4, 1, 3, -1), (3, -1, 0, 5, -1, 2), (1, 5, -1, -1, 0, 4), (4, 0, -1, -1, 5, 1), (2, -1, 5, 0, -1, 3), (-1, 3, 1, 4, 2, -1)]
ts = [i for i, x in enumerate(d) if x == a[0]]
fs = [i for i, x in enumerate(d) if x == a[1]]
b = 0
for t in ts:
    for f in fs:
        if t == f:
            continue
        r = p[t][f]
        if r == -1:
            continue
        l = [d[t], d[f], d[r], d[5-r], d[5-f], d[5-t]]
        if a == l:
            b += 1
            break
print("Yes") if b > 0 else print("No")