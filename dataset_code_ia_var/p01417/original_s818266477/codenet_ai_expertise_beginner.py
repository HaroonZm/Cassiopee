def cube_dist(a, b):
    total = 0
    for i in range(3):
        diff = a[i] - b[i]
        total += diff * diff
    return total

def cal_total_dist(t):
    if len(t) == 1:
        return 0
    total = 0
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            total += cube_dist(t[i], t[j])
    return total

def get_combinations(lst, m):
    # Simple combination generator
    def helper(start, path):
        if len(path) == m:
            result.append(tuple(path))
            return
        for i in range(start, len(lst)):
            helper(i + 1, path + [lst[i]])
    result = []
    helper(0, [])
    return result

N, M = map(int, raw_input().split())
color = []
for i in range(N):
    color.append(tuple(map(float, raw_input().split())))

comb_list = get_combinations(color, M)
max_dist = 0
for ctuple in comb_list:
    total_dist = cal_total_dist(ctuple)
    if total_dist > max_dist:
        max_dist = total_dist
print max_dist