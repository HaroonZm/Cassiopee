def cube_dist(a, b):
    s = 0
    for i in range(3):
        s += (a[i] - b[i]) ** 2
    return s

def cal_total_dist(t, dist_d):
    if len(t) == 1:
        return 0
    total = 0
    n = len(t)
    for i in range(n):
        for j in range(i+1, n):
            total += dist_d[(t[i], t[j])]
    return total

N_M = raw_input().split()
N = int(N_M[0])
M = int(N_M[1])

color = []
for i in range(N):
    vals = raw_input().split()
    color.append((float(vals[0]), float(vals[1]), float(vals[2])))

cube_dist_dict = {}
for i in range(N):
    for j in range(i+1, N):
        cube_dist_dict[(color[i], color[j])] = cube_dist(color[i], color[j])

def make_combinations(lst, m):
    res = []
    def backtrack(start, curr):
        if len(curr) == m:
            res.append(tuple(curr))
            return
        for i in range(start, len(lst)):
            backtrack(i+1, curr+[lst[i]])
    backtrack(0, [])
    return res

all_combs = make_combinations(color, M)

max_dist = 0
for ctuple in all_combs:
    td = cal_total_dist(ctuple, cube_dist_dict)
    if td > max_dist:
        max_dist = td

print max_dist