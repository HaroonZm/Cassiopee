n, m = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
res1 = a[0] - 1
res2 = n - a[-1]
res3 = []
i = 0
while i < m - 1:
    res3.append((a[i+1] - a[i]) // 2)
    i += 1
max_val = res1
if res2 > max_val:
    max_val = res2
for val in res3:
    if val > max_val:
        max_val = val
print(max_val)