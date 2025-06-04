n = int(input())
la = list(map(int, input().split()))
a = min(la)
z = max(la)
ld = []
i = a
while i <= z:
    d = 0
    j = 0
    while j < n:
        d += (la[j] - i) ** 2
        j += 1
    ld.append(d)
    i += 1
m = ld[0]
k = 1
while k < len(ld):
    if ld[k] < m:
        m = ld[k]
    k += 1
print(m)