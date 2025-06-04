n = int(input())
A = list(map(int, input().split()))
A.sort()
ex = []
if n % 2 == 1:
    ex.append(0)
    i = 0
    while i < n // 2:
        a = 2 * (i + 1)
        ex.append(a)
        ex.append(a)
        i += 1
else:
    a = 1
    i = 0
    while i < n // 2:
        ex.append(a)
        ex.append(a)
        a += 2
        i += 1
ans = 0
ok = True
i = 0
while i < n:
    if A[i] != ex[i]:
        ok = False
        break
    i += 1
if ok:
    ans = 1
    j = 0
    while j < n // 2:
        ans = (ans * 2) % (10**9 + 7)
        j += 1
print(ans)