lst = []
a, n, s = map(int, input().split())
ans = []
for i in range(1, 10001):
    if i ** n <= s:
        lst.append(i ** n)
for i in lst:
    k = str(i)
    d = a
    for j in k:
        d += int(j)
    if d ** n == i:
        ans.append(i)
print(len(ans))