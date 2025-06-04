n = int(input())
V = [0]*n
for i in [1, 2, 4]:
    s = input().split()[1:]
    for v in s:
        e = int(v)
        V[e-1] += i
c = 0
for e in V:
    if (e&4)>0 and e!=5:
        c += 1
print(c)