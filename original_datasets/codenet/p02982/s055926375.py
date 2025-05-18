from itertools import combinations
N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for a, b in combinations(X, 2):
    dist = 0
    for i in range(D):
        dist += (a[i] - b[i]) ** 2
    if dist ** 0.5 % 1 == 0:
        cnt += 1
print(cnt)