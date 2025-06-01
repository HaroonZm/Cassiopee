import copy

n = int(input())
game = n * (n-1) // 2

point = [0] * n
for _ in range(game):
    a, b, c, d = map(int, input().split())
    if c > d:
        point[a-1] += 3
    elif c < d:
        point[b-1] += 3
    else:
        point[a-1] += 1
        point[b-1] += 1

point_tmp = copy.deepcopy(point)
point_tmp.sort(reverse=True)

grade = [0] * n
for i, p in enumerate(point):
    grade[i] = point_tmp.index(p) + 1

for g in grade:
    print(g)