k_x = input().split()
k = int(k_x[0])
x = int(k_x[1])
i = x - k + 1
res = []
while i < x + k:
    res.append(i)
    i += 1
print(*res)