N, M = map(int, raw_input().split())
data = []
for i in range(N):
    line = raw_input().split()
    point = [float(x) for x in line]
    data.append(point)

result = 0.0

def get_combinations(arr, m):
    if m == 0:
        return [[]]
    if len(arr) < m:
        return []
    combs = []
    for i in range(len(arr)):
        first = arr[i]
        rest = arr[i+1:]
        for c in get_combinations(rest, m-1):
            combs.append([first] + c)
    return combs

indices = []
for i in range(N):
    indices.append(i)
all_combs = get_combinations(indices, M)

for comb in all_combs:
    dist = 0.0
    for i in range(M-1):
        for j in range(i+1, M):
            t = comb[i]
            s = comb[j]
            d = 0.0
            for k in range(3):
                d += (data[t][k] - data[s][k]) ** 2
            dist += d
    if dist > result:
        result = dist

print result