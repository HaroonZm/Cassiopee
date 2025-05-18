n, m = map(int, input().split())
A = [list(map(int, input().split())) for i in range(m)]
A.sort()
*v_min, = range(n)
*v_max, = range(n)

for _, y in A:
    v_max[y-1] = v_max[y]
    v_min[y] = v_min[y-1]

print(*[v_max[i] - v_min[i] + 1 for i in range(n)])