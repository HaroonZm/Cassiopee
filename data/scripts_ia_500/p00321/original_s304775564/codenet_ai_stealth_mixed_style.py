n, f = input().split()
n, f = int(n), int(f)
a = dict()
for _ in range(n):
    line = input().split()
    m = int(line[0])
    c = line[1:]
    for i in range(m):
        for j in range(i+1, m):
            p = tuple(sorted((c[i], c[j])))
            if p in a:
                a[p] += 1
            else:
                a.update({p:1})
b = [(k,v) for k,v in a.items() if v >= f]
b = sorted(b, key=lambda x: (x[0][0], x[0][1]))
print(len(b))
for pair, count in b:
    print(pair[0], pair[1])