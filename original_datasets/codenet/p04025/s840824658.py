n = int(input())
la = list(map(int, input().split()))

a = min(la)
z = max(la)

ld = list()
for i in range(a, z+1):
    d = 0
    for j in range(n):
        d += (la[j] - i)**2
    ld.append(d)

print(min(ld))