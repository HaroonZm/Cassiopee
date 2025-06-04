z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
inp = input()
res = []
for x in inp:
    i = z.index(x)
    n = (i - 3) % 26
    res.append(z[n])
print(*res, sep='')