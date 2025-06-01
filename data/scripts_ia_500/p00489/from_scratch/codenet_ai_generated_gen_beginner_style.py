N = int(input())
points = [0] * (N + 1)

for _ in range(N * (N - 1) // 2):
    A, B, C, D = map(int, input().split())
    if C > D:
        points[A] += 3
    elif C < D:
        points[B] += 3
    else:
        points[A] += 1
        points[B] += 1

# points[1:] contient les points des équipes 1 à N
sorted_points = sorted(points[1:], reverse=True)

ranks = [0] * (N + 1)
for i in range(N):
    # Le rang est 1 + le nombre d'équipes ayant plus de points
    rank = 1
    for sp in sorted_points:
        if sp > points[i + 1]:
            rank += 1
    ranks[i + 1] = rank

for i in range(1, N + 1):
    print(ranks[i])