n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(float, input().split())))

def get_combinations(lst, r):
    # Génère toutes les combinaisons de r éléments à partir de lst
    if r == 0:
        return [[]]
    else:
        combs = []
        for i in range(len(lst)):
            for tail in get_combinations(lst[i+1:], r-1):
                combs.append([lst[i]] + tail)
        return combs

ans = 0
combinations = get_combinations(a, m)

for p in combinations:
    sm = 0
    for i in range(m):
        for j in range(i+1, m):
            for k in range(3):
                sm += (p[i][k] - p[j][k]) ** 2
    if sm > ans:
        ans = sm

print(ans)