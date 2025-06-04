n, m = map(int, input().split())
A = []
for i in range(m):
    row = list(map(int, input().split()))
    A.append(row)
A.sort()

v_min = []
v_max = []
for i in range(n):
    v_min.append(i)
    v_max.append(i)

for pair in A:
    x = pair[0]
    y = pair[1]
    v_max[y-1] = v_max[y]
    v_min[y] = v_min[y-1]

result = []
for i in range(n):
    result.append(v_max[i] - v_min[i] + 1)

print(*result)