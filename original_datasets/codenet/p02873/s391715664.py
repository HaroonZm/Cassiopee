from itertools import groupby
x = input()
if x[0] == ">":
	x = "<" + x
if x[-1] == "<":
	x += ">"
l = [len(list(g)) for k, g in groupby(x)]
ans = 0
for i, j in zip(*[iter(l)] * 2):
	M = max(i, j)
	m = min(i, j)
	ans += M * (M + 1) // 2 + m * (m - 1) // 2
print(ans)