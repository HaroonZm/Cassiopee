n, m = map(int, input().split())
a = list(map(int, input().split()))
a.append(1000000001)
b = list(map(int, input().split()))
b.append(1000000001)
andlis = []
orlis = []
cura = 0
curb = 0
idx = 0
total = n + m
while idx < total:
    if a[cura] > b[curb]:
        orlis.append(b[curb])
        curb += 1
    elif a[cura] == b[curb]:
        andlis.append(a[cura])
        cura += 1
    else:
        orlis.append(a[cura])
        cura += 1
    idx += 1
print(len(andlis), len(orlis))
i = 0
while i < len(andlis):
    print(andlis[i])
    i += 1
j = 0
while j < len(orlis):
    print(orlis[j])
    j += 1