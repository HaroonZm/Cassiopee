from itertools import groupby
x = input()
if x[0] == ">":
    x = "<" + x
if x[-1] == "<":
    x += ">"
l = []
for k, g in groupby(x):
    l.append(len(list(g)))
ans = 0
i = 0
while i < len(l) - 1:
    a = l[i]
    b = l[i+1]
    if a > b:
        M = a
        m = b
    else:
        M = b
        m = a
    ans += M * (M + 1) // 2 + m * (m - 1) // 2
    i += 2
print(ans)