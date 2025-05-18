import bisect
n = int(input())
aas = list(map(int, input().split()))
aas.sort()
l = aas[-1]
a = l // 2
b = l // 2 + 1
idx_a = bisect.bisect_left(aas,a)
idx_b = bisect.bisect_left(aas,a)
res = []
if aas[idx_a] != l:
    res.append(idx_a)
if aas[idx_b] != l:
    res.append(idx_b)
if idx_a > 0:
    if aas[idx_a-1] != l:
        res.append(idx_a-1)
if idx_b > 0:
    if aas[idx_b-1] != l:
        res.append(idx_b-1)
if idx_a < n - 1:
    if aas[idx_a+1] != l:
        res.append(idx_a+1)
if idx_b < n - 1:
    if aas[idx_b+1] != l:
        res.append(idx_b+1)
best = l // 2
res_f = n - 1
for i in set(res):
    if abs(best-aas[i]) <= abs(best-aas[res_f]):
        res_f = i
    if l%2 != 0:
        if abs(best+1 - aas[i]) <= abs(best+1 - aas[res_f]):
            res_f = i
print(str(l)+" "+str(aas[res_f]))